DAILY_HISTORICAL_URL = '/daily_historical'

SINGLE_DAILY_HISTORICAL_POST = {
    'stockId': 1,
    'date': "2020-04-09",
            'open': 17.94,
            'high': 18.69,
            'low': 16.5,
            'close': 16.82,
            'volume': 185771300.0,
            'dividends': 0.0,
            'stockSplits': 0.0
}

SINGLE_DAILY_HISTORICAL_RESPONSE = [{
    "id": 1,
    "stockId": 1,
    "date": "2020-04-09",
    "open": 17.94,
    "high": 18.69,
    "low": 16.5,
    "close": 16.82,
    "volume": 185771300.0,
    "dividends": 0.0,
    "stockSplits": 0.0
}]

MUTIPLE_DAILY_HISTORICAL_RESPONSE = [{
    "id": 1,
    "stockId": 1,
    "date": "2020-04-09",
    "open": 17.94,
    "high": 18.69,
    "low": 16.5,
    "close": 16.82,
    "volume": 185771300.0,
    "dividends": 0.0,
    "stockSplits": 0.0
}, {
    "id": 2,
    "stockId": 2,
    "date": "2020-03-01",
    "open": 10.94,
    "high": 11.69,
    "low": 9.5,
    "close": 11.2,
    "volume": 182222300.0,
    "dividends": 0.0,
    "stockSplits": 0.0,
}]

MUTIPLE_DAILY_HISTORICAL_RESPONSE_ORDERED_DESC = [{
    "id": 2,
    "stockId": 2,
    "date": "2020-03-01",
    "open": 10.94,
    "high": 11.69,
    "low": 9.5,
    "close": 11.2,
    "volume": 182222300.0,
    "dividends": 0.0,
    "stockSplits": 0.0,
}, {
    "id": 1,
    "stockId": 1,
    "date": "2020-04-09",
    "open": 17.94,
    "high": 18.69,
    "low": 16.5,
    "close": 16.82,
    "volume": 185771300.0,
    "dividends": 0.0,
    "stockSplits": 0.0
}]

MULTIPLE_DAILY_HISTORICAL_POST = [
    {
        "stockId": 1,
        "date": "2020-04-10",
        "open": 17.94,
        "high": 18.69,
        "low": 16.5,
        "close": 16.82,
        "volume": 185771300.0,
        "dividends": 0.0,
        "stockSplits": 0.0
    },
    {
        "stockId": 1,
        "date": "2020-04-11",
        "open": 18.94,
        "high": 19.69,
        "low": 16.95,
        "close": 19.82,
        "volume": 185771300.0,
        "dividends": 0.0,
        "stockSplits": 0.0
    }]
