#!/usr/bin/python3

from datetime import datetime, timedelta
import threading
import math
import logging
import os

from flask import Flask, render_template, request

from scraping import *

app = Flask(__name__)


@app.route("/changes")
def get_changes():
    table = "gainer_timeseries"

    data = request.args.get("data")

    if data == "losers":
        table = "loser_timeseries"

    db_conn = prepare_db()

    cursor = db_conn.cursor()

    rows = []

    tickers = []

    # XXX: doing this across multiple queries is slow.
    cursor.execute("SELECT DISTINCT ON (ticker) ticker FROM {}".format(table))

    for r in cursor.fetchall():
        tickers.append(r[0])

    for t in tickers:
        cursor.execute(
            "SELECT price, volume, timestamp FROM {} WHERE ticker='{}' ORDER BY timestamp DESC LIMIT 1;".format(
                table, t
            )
        )

        r = cursor.fetchone()
        if r is not None:
            row = {
                "ticker": t,
                "cur_price": r[0],
                "volume": r[1],
            }

            rows.append(row)

    for row in rows:
        t = row["ticker"]

        one_minute_ago = datetime.now() - timedelta(minutes=1)
        one_minute_ago = math.ceil(one_minute_ago.timestamp())

        cursor.execute(
            "SELECT price FROM {} WHERE ticker='{}' AND timestamp < {} ORDER BY timestamp DESC LIMIT 1;".format(
                table, t, one_minute_ago
            )
        )

        r = cursor.fetchone()
        if r is not None:
            row["prev_price"] = r[0]

    cursor.close()

    rows = list(filter(lambda row: row.get("prev_price") is not None, rows))

    rows = sorted(
        rows, key=lambda row: row.get("cur_price") - row.get("prev_price"), reverse=True
    )

    return render_template("changes.html", rows=rows)


@app.route("/racing")
def get_racing():
    table = "gainer_timeseries"

    data = request.args.get("data")

    if data == "losers":
        table = "loser_timeseries"

    db_conn = prepare_db()

    cursor = db_conn.cursor()

    rows = []

    tickers = []

    # FIXME: code duplication with get_changes and bad perf.
    cursor.execute("SELECT DISTINCT ON (ticker) ticker FROM {}".format(table))

    for r in cursor.fetchall():
        tickers.append(r[0])

    for t in tickers:
        cursor.execute(
            "SELECT price, volume, timestamp FROM {} WHERE ticker='{}' ORDER BY timestamp DESC LIMIT 1;".format(
                table, t
            )
        )

        r = cursor.fetchone()
        if r is not None:
            row = {
                "ticker": t,
                "cur_price": r[0],
                "volume": r[1],
            }

            rows.append(row)

    for row in rows:
        t = row["ticker"]

        five_minutes_ago = datetime.now() - timedelta(minutes=5)
        five_minutes_ago = math.ceil(five_minutes_ago.timestamp())

        cursor.execute(
            "SELECT price FROM {} WHERE ticker='{}' AND timestamp < {} ORDER BY timestamp DESC LIMIT 1;".format(
                table, t, five_minutes_ago
            )
        )

        r = cursor.fetchone()
        if r is not None:
            row["prev_price"] = r[0]
        else:
            row["prev_price"] = -1

    cursor.close()

    sorted_rows1 = sorted(rows, key=lambda row: row.get("cur_price"), reverse=True)
    sorted_rows2 = sorted(rows, key=lambda row: row.get("prev_price"), reverse=True)

    for i in range(len(sorted_rows1)):
        row = sorted_rows1[i]
        row["cur_pos"] = i + 1

    for i in range(len(sorted_rows2)):
        row = sorted_rows2[i]
        row["prev_pos"] = i + 1

    rows = sorted(rows, key=lambda row: row.get("cur_pos"))

    return render_template("racing.html", rows=rows)


@app.route("/")
def index():
    return render_template("index.html")


def main():
    logging.basicConfig(
        format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s",
        level=logging.DEBUG,
    )

    tw = threading.Thread(target=run_loop_winner, daemon=True)
    tl = threading.Thread(target=run_loop_loser, daemon=True)

    logging.info("Launching run loop threads...")

    tw.start()

    t = threading.Timer(30.0, tl.start)
    t.start()

    port = 80
    if os.environ.get("PORT") is not None:
        port = os.environ.get("PORT")

    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()