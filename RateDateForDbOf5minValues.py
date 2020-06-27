from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import datetime
import json


def getting_rate_date():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start': '1',
      'limit': '5000',
      'convert': 'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '000de33c-f464-4660-ae72-ef4a47a11a68',
    }

    session = Session()
    session.headers.update(headers)

    try:
        date = str(datetime.datetime.now())[:-10]
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        rate = data['data'][0]['quote']['USD']['price']
        return date, rate
    except:
        return 'Ошибка'

