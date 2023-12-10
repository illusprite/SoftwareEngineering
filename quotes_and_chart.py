from datetime import datetime, timedelta
from pandas import DataFrame
from ta.trend import ema_indicator
from tinkoff.invest import Client, RequestError, CandleInterval, HistoricCandle

import creds
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def run(figi, time):
    try:
        with Client(creds.tok) as client:
            info = get_time_information(time)
            r = client.market_data.get_candles(
                figi=figi,  # figi финансового инстромента (валюты, акции...)
                from_ = info[0],
                to=datetime.utcnow(),
                interval= info[1]
            )
            df = create_df(r.candles)
            df['ema'] = ema_indicator(close=df['close'], window=9)

            print(df[['Время', 'close', 'ema']].tail(30)) #Tail - чтобы сократить вывод до 30 строк, остальное ен показывается
            ax = df.plot(x='Время', y='close')
            df.plot(ax=ax, x='Время', y='ema')
            plt.show()

    except RequestError as e:
        print(str(e))

def get_time_information(time):
    try:
        with Client(creds.tok) as client:
            if time == 1:
                # День
                from_ = datetime.utcnow() - timedelta(weeks=1)
                interval = CandleInterval.CANDLE_INTERVAL_HOUR
                return [from_, interval]

            elif time == 2:
                # Месяц
                from_ = datetime.utcnow() - timedelta(days=30)
                interval = CandleInterval.CANDLE_INTERVAL_DAY
                return [from_, interval]

            elif time == 3:
                # Год
                from_ = datetime.utcnow() - timedelta(days=365)
                interval = CandleInterval.CANDLE_INTERVAL_DAY
                return [from_, interval]

    except RequestError as e:
        print(str(e))

def create_df(candles: [HistoricCandle]):
    df = DataFrame([{
        'Время': c.time,
        'volume': c.volume,
        'open': cast_money(c.open),
        'close': cast_money(c.close),
        'high': cast_money(c.high),
        'low': cast_money(c.low),
    } for c in candles])

    return df

def cast_money(v):
    """
    https://tinkoff.github.io/investAPI/faq_custom_types/
    :param v:
    :return:
    """
    return v.units + v.nano / 1e9  # nano - 9 нулей
