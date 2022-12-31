import MetaTrader5 as mt5
import pandas as pd
import datetime
import time


def signal(symbol, timeframe, sma_period):
    bars = mt5.copy_rates_from_pos(symbol, timeframe, 1, sma_period)
    bars_df = pd.DataFrame(bars)

    last_close = bars_df.iloc[-1].close
    sma = bars_df.close.mean()

    # direction = 'flat'
    # if last_close > sma:
    #     direction = 'buy'
    # elif last_close < sma:
    #     direction = 'sell'

    return last_close, sma#, direction


if __name__ == '__main__':
    #Parametros de la estrategia
    SYMBOL = "GBPUSD"
    VOLUME = 1.0
    TIMEFRAME = mt5.TIMEFRAME_M1
    SMA_PERIOD = 10
    DEVIATION = 20

    mt5.initialize()

    for i in range(1):
        last_close, sma = signal(SYMBOL, TIMEFRAME, SMA_PERIOD)
        print(last_close)
        print(sma)