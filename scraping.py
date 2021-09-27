#!/usr/bin/python3

import base64
import configparser
from datetime import datetime
from pprint import pprint
import string
import os
import threading
import time
import logging
import json

import requests
import psycopg2
from lxml import html
import js2xml
import websocket

from PricingData_pb2 import *

config = configparser.ConfigParser()

config.read("config.ini")

HOST = config["PostgreSQL"]["Host"]
USER_NAME = config["PostgreSQL"]["Username"]
PASSWORD = config["PostgreSQL"]["Password"]
DATABASE_NAME = config["PostgreSQL"]["Database"]

TOP_GAINER_SCREENER_URL = "https://finance.yahoo.com/screener/predefined/day_gainers?offset=0&count=50&guccounter=1"
TOP_GAINER_JSON_DICT = {
    "offset": 0,
    "size": 50,
    "sortField": "percentchange",
    "sortType": "DESC",
    "quoteType": "EQUITY",
    "query": {
        "operator": "AND",
        "operands": [
            {"operator": "GT", "operands": ["percentchange", 3]},
            {"operator": "eq", "operands": ["region", "us"]},
            {
                "operator": "or",
                "operands": [
                    {
                        "operator": "BTWN",
                        "operands": ["intradaymarketcap", 2000000000, 10000000000],
                    },
                    {
                        "operator": "BTWN",
                        "operands": [
                            "intradaymarketcap",
                            10000000000,
                            100000000000,
                        ],
                    },
                    {
                        "operator": "GT",
                        "operands": ["intradaymarketcap", 100000000000],
                    },
                ],
            },
            {"operator": "gt", "operands": ["dayvolume", 15000]},
        ],
    },
    "userId": "",
    "userIdType": "guid",
}

TOP_LOSER_SCREENER_URL = (
    "https://finance.yahoo.com/screener/predefined/day_losers?offset=0&count=50"
)
TOP_LOSER_JSON_DICT = {
    "offset": 0,
    "size": 50,
    "sortField": "percentchange",
    "sortType": "ASC",
    "quoteType": "EQUITY",
    "query": {
        "operator": "AND",
        "operands": [
            {"operator": "LT", "operands": ["percentchange", -2.5]},
            {"operator": "eq", "operands": ["region", "us"]},
            {
                "operator": "or",
                "operands": [
                    {
                        "operator": "BTWN",
                        "operands": ["intradaymarketcap", 2000000000, 10000000000],
                    },
                    {
                        "operator": "BTWN",
                        "operands": [
                            "intradaymarketcap",
                            10000000000,
                            100000000000,
                        ],
                    },
                    {
                        "operator": "GT",
                        "operands": ["intradaymarketcap", 100000000000],
                    },
                ],
            },
            {"operator": "gt", "operands": ["dayvolume", 20000]},
        ],
    },
    "userId": "",
    "userIdType": "guid",
}


def create_yahoo_session():
    session = requests.Session()
    session.headers = {
        "pragma": "no-cache",
        "cache-control": "no-cache",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "sec-fetch-site": "none",
        "sec-fetch-mode": "navigate",
        "sec-fetch-user": "?1",
        "sec-fetch-dest": "document",
        "accept-language": "en-GB,en;q=0.9,en-US;q=0.8,lt;q=0.7",
    }

    resp = session.get("https://finance.yahoo.com/")
    tree = html.fromstring(resp.text)

    form_data = {"agree": "agree"}

    for hidden_input in tree.xpath('//input[@type="hidden"]'):
        form_data[hidden_input.get("name")] = hidden_input.get("value")

    url = "https://consent.yahoo.com/v2/collectConsent"
    params = {"sessionId": form_data.get("sessionId")}

    resp = session.post(url, params=params, data=form_data)

    logging.debug(session.cookies)

    return session


def get_tickers(session, screener_url, json_dict,db_table):
    tickers = []

    resp0 = session.get(screener_url)
    logging.info(resp0.url)

    tree = html.fromstring(resp0.text)

    js = tree.xpath('//script[contains(text(), "CrumbStore")]')
    js = js[0]

    js = js.text

    parsed = js2xml.parse(js)

    crumb = parsed.xpath(
        '//property[@name="CrumbStore"]/object/property[@name="crumb"]/string/text()'
    )[0]

    logging.debug("Got crumb: {}".format(crumb))

    params = {
        "crumb": crumb,
        "lang": "en-US",
        "region": "US",
        "formatted": "true",
        "corsDomain": "finance.yahoo.com",
    }

    resp = session.post(
        "https://query1.finance.yahoo.com/v1/finance/screener",
        json=json_dict,
        params=params,
    )
    logging.info(resp.url)

    json_dict = resp.json()

    result = json_dict.get("finance", dict()).get("result")
    if result is None:
        return []

    result = result[0]

    count = result.get("count")

    quotes = result.get("quotes")

    for quote_dict in quotes:
        symbol = quote_dict.get("symbol")
        if len(symbol) <= 4:
            tickers.append(symbol)
        
    db_conn = prepare_db()
    cursor = db_conn.cursor()
    if db_table:
        table = db_table
        cursor.execute("SELECT DISTINCT ON (ticker) ticker FROM {}".format(table))
        for r in cursor.fetchall():
            if r not in tickers:
                tickers.append(r[0])

    return tickers


def prepare_db():
    if os.environ.get("DATABASE_URL") is not None:
        DATABASE_URL = os.environ["DATABASE_URL"]
        db_conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    else:
        db_conn = psycopg2.connect(
            host=HOST, user=USER_NAME, password=PASSWORD, dbname=DATABASE_NAME
        )

    cursor = db_conn.cursor()

    try:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS gainer_timeseries (ticker TEXT, price FLOAT, timestamp FLOAT, volume FLOAT)"
        )
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS loser_timeseries (ticker TEXT, price FLOAT, timestamp FLOAT, volume FLOAT)"
        )
    except Exception as e:
        logging.error(e)

    cursor.close()
    db_conn.commit()

    return db_conn


def run_loop(screener_url, json_dict, db_table):
    db_conn = prepare_db()
    cursor = db_conn.cursor()

    session = create_yahoo_session()

    while True:
        try:
            tickers = get_tickers(session, screener_url, json_dict,db_table)
        except Exception as e:
            session = create_yahoo_session()
            logging.error(e)
            continue

        request = {"subscribe": tickers}

        ws = websocket.WebSocket()
        ws.connect("wss://streamer.finance.yahoo.com/")

        ws.send(json.dumps(request))
        tickers_refreshed_at = datetime.now()

        while True:
            try:
                got_msg = ws.recv()
            except Exception as e:
                logging.error(e)
                break

            pricing_data = PricingData()

            pricing_data.ParseFromString(base64.b64decode(got_msg))
            logging.info(
                "{} {} {} {} {}".format(
                    datetime.utcfromtimestamp(pricing_data.time / 1000).strftime(
                        "%Y-%m-%d %H:%M:%S"
                    ),
                    pricing_data.price,
                    pricing_data.exchange,
                    pricing_data.id,
                    pricing_data.dayVolume,
                )
            )

            ticker = pricing_data.id
            price = pricing_data.price
            timestamp = round(pricing_data.time / 1000)
            volume = pricing_data.dayVolume
            if price < 100 or price > 1000:
                continue
            cursor.execute("BEGIN")
            try:
                cursor.execute(
                    "DELETE FROM {} WHERE ticker='{}' AND timestamp={}".format(
                        db_table, ticker, timestamp
                    )
                )
            except Exception:
                print(Exception, "Exception occured -1")

            try:
                cursor.execute(
                    "INSERT INTO {} (ticker, price, timestamp, volume) VALUES ('{}', {}, {}, {})".format(
                        db_table, ticker, price, timestamp, volume
                    )
                )
            except Exception:
                print(Exception, "Exception occured - 2")

            try:    
                cursor.execute(
                    "DELETE FROM {} WHERE ticker='{}' AND timestamp < {}".format(
                        db_table, ticker, timestamp - 10 * 60
                    )
                )
            except Exception:
                print(Exception, "Exception occured - 3")

            cursor.execute("COMMIT")
            db_conn.commit()
            
            now = datetime.now()
            delta = now - tickers_refreshed_at

            if delta.total_seconds() > 10 * 60:
                logging.info("10 minutes elapsed - refreshing ticker list")
                ws.close()
                break


def run_loop_winner():
    while True:
        run_loop(TOP_GAINER_SCREENER_URL, TOP_GAINER_JSON_DICT, "gainer_timeseries")


def run_loop_loser():
    while True:
        run_loop(TOP_LOSER_SCREENER_URL, TOP_LOSER_JSON_DICT, "loser_timeseries")


def main():
    logging.basicConfig(
        format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
        level=logging.DEBUG,
    )

    tw = threading.Thread(target=run_loop_winner, daemon=True)
    tl = threading.Thread(target=run_loop_loser, daemon=True)

    logging.info("Launching run loop threads...")

    tw.start()
    time.sleep(30)
    tl.start()

    tw.join()
    tl.join()


if __name__ == "__main__":
    main()
