#!/usr/bin/python3

from datetime import datetime, timedelta
import threading
import math
import logging
import os
import pymongo

from flask import Flask, render_template, request

from db import prepare_db

app = Flask(__name__)


@app.route("/changes")
def get_changes():
    table = "gainer_timeseries"

    data = request.args.get("data")

    if data == "losers":
        table = "loser_timeseries"

    db_conn,client = prepare_db()


    # cursor = db_conn.cursor()

    rows = []

    tickers = []

    # XXX: doing this across multiple queries is slow.
    # cursor.execute("SELECT DISTINCT ON (ticker) ticker FROM {}".format(table))

    for ticker in db_conn[table].distinct('ticker'):
        tickers.append(ticker)

    for t in tickers:
        # cursor.execute(
        #     "SELECT price, volume, timestamp FROM {} WHERE ticker='{}' ORDER BY timestamp DESC LIMIT 1;".format(
        #         table, t
        #     )
        # )

        # r = cursor.fetchone()
        query = {
            "$query": {"ticker": t},
            "$orderby": {"timestamp": -1}
        }
        ticker = db_conn[table].find_one(query)
        if ticker is not None:
            row = {
                "ticker": t,
                "cur_price": ticker["price"],
                "volume": ticker["volume"],
            }
            rows.append(row)

    for row in rows:
        t = row["ticker"]

        one_minute_ago = datetime.now() - timedelta(minutes=1)
        one_minute_ago = math.ceil(one_minute_ago.timestamp())

        # cursor.execute(
        #     "SELECT price FROM {} WHERE ticker='{}' AND timestamp < {} ORDER BY timestamp DESC LIMIT 1;".format(
        #         table, t, one_minute_ago
        #     )
        # )

        # r = cursor.fetchone()
        query = {
            "$query": {"ticker": t, "timestamp": {"$lte": one_minute_ago}},
            "$orderby": {"timestamp": -1}
        }
        ticker = db_conn[table].find_one(query)
        if ticker is not None:
            row["prev_price"] = ticker['price']

    # cursor.close()

    rows = list(filter(lambda row: row.get("prev_price") is not None, rows))

    rows = sorted(
        rows, key=lambda row: row.get("cur_price") - row.get("prev_price"), reverse=True
    )
    client.close()
    return render_template("changes.html", rows=rows)


@app.route("/racing")
def get_racing():
    table = "gainer_timeseries"

    data = request.args.get("data")

    if data == "losers":
        table = "loser_timeseries"

    db_conn,client = prepare_db()

    # cursor = db_conn.cursor()

    rows = []

    tickers = []

    # FIXME: code duplication with get_changes and bad perf.
    # cursor.execute("SELECT DISTINCT ON (ticker) ticker FROM {}".format(table))
    for ticker in db_conn[table].distinct('ticker'):
        tickers.append(ticker)
    # for r in cursor.fetchall():
    #     tickers.append(r[0])

    for t in tickers:
        query = {
            "$query": {"ticker": t},
            "$orderby": {"timestamp": -1}
        }
        ticker = db_conn[table].find_one(query)
        if ticker is not None:
            row = {
                "ticker": t,
                "cur_price": ticker["price"],
                "volume": ticker["volume"],
            }
            rows.append(row)

    for row in rows:
        t = row["ticker"]

        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        five_minutes_ago = math.ceil(five_minutes_ago.timestamp())

        # cursor.execute(
        #     "SELECT price FROM {} WHERE ticker='{}' AND timestamp < {} ORDER BY timestamp DESC LIMIT 1;".format(
        #         table, t, five_minutes_ago
        #     )
        # )

        # r = cursor.fetchone()
        query = {
            "$query": {"ticker": t, "timestamp": {"$lte": five_minutes_ago}},
            "$orderby": {"timestamp": -1}
        }
        ticker = db_conn[table].find_one(query)
        if ticker is not None:
            row["prev_price"] = ticker['price']
        else:
            row["prev_price"] = -1

    # cursor.close()

    sorted_rows1 = sorted(
        rows, key=lambda row: row.get("cur_price"), reverse=True)
    sorted_rows2 = sorted(
        rows, key=lambda row: row.get("prev_price"), reverse=True)

    for i in range(len(sorted_rows1)):
        row = sorted_rows1[i]
        row["cur_pos"] = i + 1

    for i in range(len(sorted_rows2)):
        row = sorted_rows2[i]
        row["prev_pos"] = i + 1

    rows = sorted(rows, key=lambda row: row.get("cur_pos"))
    client.close()
    return render_template("racing.html", rows=rows)


@app.route("/gapper")
def get_gapper():
    table = "gainer_timeseries"

    data = request.args.get("data")

    if data == "losers":
        table = "loser_timeseries"

    db_conn,client = prepare_db()

    # cursor = db_conn.cursor()

    rows = []

    tickers = []

    # FIXME: code duplication with get_changes and bad perf.
    # cursor.execute("SELECT DISTINCT ON (ticker) ticker FROM {}".format(table))

    # for r in cursor.fetchall():
    #     tickers.append(r[0])
    for ticker in db_conn[table].distinct('ticker'):
        tickers.append(ticker)

    for t in tickers:
        # cursor.execute(
        #     "SELECT price, volume, timestamp FROM {} WHERE ticker='{}' ORDER BY timestamp DESC LIMIT 1;".format(
        #         table, t
        #     )
        # )

        # r = cursor.fetchone()
        query = {
            "$query": {"ticker": t},
            "$orderby": {"timestamp": -1}
        }
        ticker = db_conn[table].find_one(query)
        if ticker is not None:
            if round(ticker['price'], 3) < 100 or round(ticker['price'], 3) > 1000:
                continue
            row = {
                "ticker": t,
                "cur_price": ticker["price"],
                "volume": ticker["volume"],
            }
            rows.append(row)

    for row in rows:
        t = row["ticker"]

        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        five_minutes_ago = math.ceil(five_minutes_ago.timestamp())

        # cursor.execute(
        #     "SELECT price FROM {} WHERE ticker='{}' AND timestamp < {} ORDER BY timestamp DESC LIMIT 1;".format(
        #         table, t, five_minutes_ago
        #     )
        # )

        # ticker = cursor.fetchone()
        query = {
            "$query": {"ticker": t, "timestamp": {"$lte": five_minutes_ago}},
            "$orderby": {"timestamp": -1}
        }
        ticker = db_conn[table].find_one(query)
        if ticker is not None:
            row["prev_price"] = ticker['price']
        else:
            row["prev_price"] = -1

    # cursor.close()

    sorted_rows1 = sorted(
        rows, key=lambda row: row.get("cur_price"), reverse=True)
    sorted_rows2 = sorted(
        rows, key=lambda row: row.get("prev_price"), reverse=True)

    for i in range(len(sorted_rows1)):
        row = sorted_rows1[i]
        row["cur_pos"] = i + 1

    for i in range(len(sorted_rows2)):
        row = sorted_rows2[i]
        row["prev_pos"] = i + 1

    for row in rows:
        row["gapper"] = row["prev_pos"] - row["cur_pos"]

    rows = sorted(rows, key=lambda row: row.get("gapper"))
    client.close()
    return render_template("gapper.html", rows=rows)


@app.route("/volatility")
def get_volatility():
    tables = ["gainer_timeseries", "loser_timeseries"]
    db_conn,client = prepare_db()
    rows = []
    tickers = []
    for table in tables:
        tickers = []
        table_rows = []
        for ticker in db_conn[table].distinct('ticker'):
            tickers.append(ticker)
        for t in tickers:
            query = {
                "$query": {"ticker": t},
                "$orderby": {"timestamp": -1}
            }
            ticker = db_conn[table].find_one(query)
            if ticker is not None:
                if round(ticker['price'], 3) < 100 or round(ticker['price'], 3) > 1000:
                    continue
                row = {
                    "ticker": t,
                    "cur_price": ticker["price"],
                    "volume": ticker["volume"],
                }
                if row in rows:
                    continue
                table_rows.append(row)
        new_rows = []
        for row in table_rows:
            t = row["ticker"]
            two_minutes_ago = datetime.now() - timedelta(minutes=2)
            two_minutes_ago = math.ceil(two_minutes_ago.timestamp())
            query = {
                "$query": {"ticker": t, "timestamp": {"$lte": two_minutes_ago}},
                "$orderby": {"timestamp": -1}
            }
            ticker = db_conn[table].find_one(query)
            if ticker == None:
                query = {
                    "$query": {"ticker": t},
                    "$orderby": {"timestamp": 1}
                }
                ticker = db_conn[table].find_one(query)
                if ticker is None:
                    continue
            row["prev_price"] = ticker['price']
            row["price_change"] = round(
                abs(row["cur_price"] - row["prev_price"]), 3)
            row["prev_price"] = round(row["prev_price"], 3)
            row["cur_price"] = round(row["cur_price"], 3)
            new_rows.append(row)
        rows.extend(new_rows)
    rows = sorted(rows, key=lambda row: row.get("price_change"))
    row_ticker = []
    for index in range(len(rows)):
        if rows[index]["ticker"] in row_ticker:
            del rows[index]
        else:
            row_ticker.append(rows[index]["ticker"])
    client.close()
    return render_template("volatility.html", rows=rows)


@app.route("/")
def index():
    return render_template("index.html")


def main():
    # logging.basicConfig(
    #     format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
    #     level=logging.DEBUG,
    # )

    # tw = threading.Thread(target=run_loop_winner, daemon=True)
    # tl = threading.Thread(target=run_loop_loser, daemon=True)

    logging.info("Launching run loop threads...")

    # tw.start()

    # t = threading.Timer(30.0, tl.start)
    # t.start()

    port = 80
    if os.environ.get("PORT") is not None:
        port = os.environ.get("PORT")

    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
