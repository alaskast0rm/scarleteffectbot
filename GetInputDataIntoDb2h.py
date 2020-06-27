import datetime
import json
import sqlite3
from requests import Session
from time import sleep


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
        date = str(datetime.datetime.now() + datetime.timedelta(hours=3))[:-10]
        print(date)
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        rate = data['data'][0]['quote']['USD']['price']
        return date, rate
    except:
        return 'Error'


while True:
    received_data = getting_rate_date()

    if len(received_data) == 2:
        received_date = received_data[0]
        received_rate = str(received_data[1])

        conn = sqlite3.connect('DbOf2HourValues.db')

        c = conn.cursor()

        c.execute("INSERT INTO BTC VALUES (?, ?)", (received_date, received_rate))

        # c.execute("SELECT * FROM BTC WHERE date LIKE '{}%'".format(received_date))
        #
        # print(c.fetchall())

        conn.commit()

        conn.close()

        sleep(7200)