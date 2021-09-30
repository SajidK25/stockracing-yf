#!/usr/bin/python3

import base64
import configparser
from datetime import datetime
from pprint import pprint
import string
import os
import yliveticker
import threading
import time
import logging
import json
from threading import Timer
import requests
import psycopg2
from lxml import html
import js2xml
import websocket
import pymongo
from PricingData_pb2 import *
from db import prepare_db

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
        
    db,client = prepare_db()
    # cursor = db_conn.cursor()

    if db_table:
        # table = db_table
        # cursor.execute("SELECT DISTINCT ON (ticker) ticker FROM {}".format(table))
        for r in db[db_table].distinct('ticker'):
            if r not in tickers:
                tickers.append(r[0])
    client.close()
    return tickers


def insert_db_gainer(ws,pricing_data):
    db,client = prepare_db()
    db_table = "gainer_timeseries"
    logging.info(
        "{} {} {} {} {}".format(
            datetime.utcfromtimestamp(pricing_data["timestamp"] / 1000).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            pricing_data["price"],
            pricing_data["exchange"],
            pricing_data["id"],
            pricing_data["dayVolume"],
        )
    )
    ticker = pricing_data["id"]
    price = round(pricing_data["price"],3)
    timestamp = round(pricing_data["timestamp"] / 1000)
    volume = pricing_data["dayVolume"]
    if price < 100 or price > 1000:
        return
    try:
        db[db_table].delete_many({"ticker":ticker,"timestamp":timestamp})
    except Exception:
        print(Exception, "Exception occured -1")

    try:
        db[db_table].insert_one({
            "ticker":ticker,
            "price":price,
            "timestamp":timestamp,
            "volume":volume
        })
    except Exception:
        print(Exception, "Exception occured - 2")

    try:    
        result = db[db_table].delete_many({
            "timestamp" : {"$lt" : timestamp - 10 * 60 }
        })
        logging.info(f"Deleted {result.deleted_count} records")
    except Exception:
        print(Exception, "Exception occured - 3")
    client.close()
    now = datetime.now()
    delta = now - timing[db_table]

    if delta.total_seconds() > 10 * 60:
        logging.info("10 minutes elapsed - refreshing ticker list")
        ws.close()

def insert_db_loser(ws,pricing_data):
    db,client = prepare_db()
    db_table = "loser_timeseries"
    logging.info(
        "{} {} {} {} {}".format(
            datetime.utcfromtimestamp(pricing_data["timestamp"] / 1000).strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            pricing_data["price"],
            pricing_data["exchange"],
            pricing_data["id"],
            pricing_data["dayVolume"],
        )
    )
    ticker = pricing_data["id"]
    price = round(pricing_data["price"],3)
    timestamp = round(pricing_data["timestamp"] / 1000)
    volume = pricing_data["dayVolume"]
    if price < 100 or price > 1000:
        return
    try:
        db[db_table].delete_many({"ticker":ticker,"timestamp":timestamp})
    except Exception:
        print(Exception, "Exception occured -1")

    try:
        db[db_table].insert_one({
            "ticker":ticker,
            "price":price,
            "timestamp":timestamp,
            "volume":volume
        })
    except Exception:
        print(Exception, "Exception occured - 2")

    try:
        result = db[db_table].delete_many({
            "timestamp" : {"$lt" : timestamp - 1 * 60 }
        })
        logging.info(f"Deleted {result.deleted_count} records")
    except Exception:
        print(Exception, "Exception occured - 3")
    client.close()
    now = datetime.now()
    delta = now - timing[db_table]

    if delta.total_seconds() > 1 * 60:
        logging.info("10 minutes elapsed - refreshing ticker list")
        ws.close()

timing = {}

def onexit(*args, **kwargs):
    print("Exiting")
    print(kwargs)

def run_loop(screener_url, json_dict, db_table):
    session = create_yahoo_session()

    while True:
        try:
            tickers = get_tickers(session, screener_url, json_dict,db_table)
            print(db_table)
        except Exception as e:
            session = create_yahoo_session()
            logging.error(e)
            continue
        print(tickers)
        timing[db_table] = datetime.now()
        if db_table == "gainer_timeseries":
            yliveticker.YLiveTicker(on_ticker=insert_db_gainer, ticker_names=tickers,on_close=onexit,on_error=onexit)
        else:
            yliveticker.YLiveTicker(on_ticker=insert_db_loser, ticker_names=tickers,on_close=onexit)

def run_loop_winner():
    while True:
        run_loop(TOP_GAINER_SCREENER_URL, TOP_GAINER_JSON_DICT, "gainer_timeseries")


def run_loop_loser():
    while True:
        # run_loop(TOP_LOSER_SCREENER_URL, TOP_LOSER_JSON_DICT, "loser_timeseries")
        pass


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
