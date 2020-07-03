import datetime
import sqlite3
from time import sleep
from bs4 import BeautifulSoup as bs
from requests import Session


headers = {'accept': '*/*',
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/"


def get_rate_date():
    session = Session()
    request = session.get(url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        data = soup.find('tbody').find('tr').find_all('td')
        high_rate = data[2].text[:-3].replace(',', '')
        low_rate = data[3].text[:-3].replace(',', '')
        average_rate = (int(high_rate) + int(low_rate)) // 2
        date = (datetime.datetime.now() + datetime.timedelta(hours=3)).strftime("%Y-%d-%m %H:%M")
        return date, average_rate
    else:
        return 'Error'


while True:
    received_data = get_rate_date()

    if len(received_data) == 2:
        received_date = received_data[0]
        received_rate = str(received_data[1])

        conn = sqlite3.connect('DbOf24HourValues.db')

        c = conn.cursor()

        c.execute("INSERT INTO BTC VALUES(?, ?)", (received_date, received_rate))

        conn.commit()

        conn.close()

        sleep(86400)
