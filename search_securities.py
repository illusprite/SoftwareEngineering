from pandas import DataFrame
from tinkoff.invest.services import InstrumentsService, MarketDataService
import creds
from tinkoff.invest import Client, InstrumentStatus, RequestError

def search_all_securities(choice_type):
    try:
        with Client(creds.tok) as client:
            instruments: InstrumentsService = client.instruments
            market_data: MarketDataService = client.market_data

            if choice_type == 1:
                r = DataFrame(instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments,
                              columns=['name', 'figi', 'ticker', 'class_code'])
                return r
            elif choice_type == 2:
                r = DataFrame(instruments.bonds(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments,
                              columns=['name', 'figi', 'ticker', 'class_code'])
                return r
            else:
                r = DataFrame(instruments.currencies(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments,
                              columns=['name', 'figi', 'ticker', 'class_code'])
                return r
            #r = r[r['ticker'] == choice_ticker]
    except RequestError as e:
        print(str(e))



def search_figi_securities(choice_ticker, choice_type):
    try:
        with Client(creds.tok) as client:
            instruments: InstrumentsService = client.instruments
            market_data: MarketDataService = client.market_data

            if choice_type == 1:
                r = DataFrame(instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments,
                              columns=['name', 'figi', 'ticker', 'class_code'])
                r = r[r['ticker'] == choice_ticker]['figi'].iloc[0]
                return r
            elif choice_type == 2:
                r = DataFrame(instruments.bonds(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments,
                              columns=['name', 'figi', 'ticker', 'class_code'])
                r = r[r['ticker'] == choice_ticker]['figi'].iloc[0]
                return r
            else:
                r = DataFrame(instruments.currencies(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments,
                              columns=['name', 'figi', 'ticker', 'class_code'])
                r = r[r['ticker'] == choice_ticker]['figi'].iloc[0]
                return r

    except RequestError as e:
        print(str(e))

