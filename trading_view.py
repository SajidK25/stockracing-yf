from tradingview_ta import TA_Handler, Interval, Exchange,TradingView
import tradingview_ta


def get_analysis(ticker):
    handler  = TA_Handler(
        symbol=ticker,
        screener="america",
        exchange="nasdaq",
        interval=Interval.INTERVAL_1_DAY,
        timeout=None,
    )
    try:
        analysis = handler.get_analysis()
    except:
        return None
    print(ticker + " - " + str(analysis.indicators["ADX"]))
    return analysis.indicators