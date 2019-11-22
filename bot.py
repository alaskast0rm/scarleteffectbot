from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import requests
from bs4 import BeautifulSoup as bs
import random

TG_TOKEN = '968188661:AAEF4JBqD5OzPDK9I2LfTeQp-Jlr_Zd37u4'
head = {'accept': '*/*',
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}


def message_handler(bot: Bot, update: Update):
	user = update.effective_user

	if user:
		name = user.first_name
	else:
		name = 'анонимыч'
	text = update.effective_message.text
	reply_text = f'Ну здарова {name}\n\n{text}'

	if '/dol' in text:
		headers = head
		url = 'https://www.banki.ru/products/currency/usd/'

		sesion = requests.Session()
		request = sesion.get(url, headers=headers)
		if request.status_code == 200:
			soup = bs(request.content, 'html.parser')
			divs = soup.find_all('div', attrs={'class': 'layout-columns-wrapper'})
			print('ok')

			for div in divs:
				divka = div.find('div', attrs={'class': "currency-table__large-text"}).text
				divka1 = divka + 'RUB за 1$'
				reply_text = divka1
		bot.send_message(
			chat_id=update.effective_message.chat_id,
			text=reply_text,
		)

	if '/pyhh' in text:
		url = 'https://hh.ru/search/vacancy?only_with_salary=false&clusters=true&area=1&enable_snippets=true&salary=&st=searchVacancy&text=Python+junior'
		headers = head
		session = requests.Session()
		request = session.get(url, headers=headers)

		if request.status_code == 200:
			soup = bs(request.content, 'html.parser')
			divs = soup.find_all('div', attrs={'data-qa': "vacancy-serp__vacancy"})
			counter = 0
			response = ''
			for div in divs:
				counter += 1
				divka = div.find('div', attrs={'class': "vacancy-serp-item__row vacancy-serp-item__row_header"}).text
				divka_https = div.find('a', href=True)
				mod_divka_https = divka_https['href']

				def result(divka):
					return '\n'.join(str(divka) for i in range(1))

				def result_https(mod_divka_https):
					return '\n'.join(str(mod_divka_https) for i in range(1))

				response += f'{counter}) ' + str(result(divka)) + f"\n{result_https(mod_divka_https)}\n"
			reply_text = response

			bot.send_message(
				chat_id=update.effective_message.chat_id,
				text=reply_text,
			)

	if '/adhh' in text:
		url = 'https://hh.ru/search/vacancy?only_with_salary=false&clusters=true&area=1&enable_snippets=true&salary=&st=searchVacancy&text=%D0%9C%D0%BB%D0%B0%D0%B4%D1%88%D0%B8%D0%B9+%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%BD%D1%8B%D0%B9+%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80&from=suggest_post'
		headers = head
		session = requests.Session()
		request = session.get(url, headers=headers)

		if request.status_code == 200:
			soup = bs(request.content, 'html.parser')
			divs = soup.find_all('div', attrs={'data-qa': "vacancy-serp__vacancy"})
			counter = 0
			response = ''
			for div in divs:
				counter += 1
				divka = div.find('div', attrs={'class': "vacancy-serp-item__row vacancy-serp-item__row_header"}).text
				divka_https = div.find('a', href=True)
				mod_divka_https = divka_https['href']

				def result(divka):
					return '\n'.join(str(divka) for i in range(1))

				def result_https(mod_divka_https):
					return '\n'.join(str(mod_divka_https) for i in range(1))

				response += f'{counter}) ' + str(result(divka)) + f"\n{result_https(mod_divka_https).split('?')[0]}\n"
			reply_text = response

			bot.send_message(
				chat_id=update.effective_message.chat_id,
				text=reply_text,
			)

	if '/cat' in text:
		url = 'https://random.cat/view/'
		number = random.randint(1, 1500)
		reply_text = url + str(number)
		bot.send_photo(
			chat_id=update.effective_message.chat_id,
			photo=reply_text,
		)

	if '/bc' in text:
		photo_url = "https://www.tradingview.com/x/2D4tS4y6"
		bot.send_photo(
			chat_id=update.effective_message.chat_id,
			photo=photo_url,
		)

	if '/weather' in text:
		url = "https://yandex.ru/pogoda/moscow"
		headers = head
		session = requests.Session()
		request = session.get(url, headers=headers)

		if request.status_code == 200:
			soup = bs(request.content, 'html.parser')
			divs = soup.find_all('div', attrs={'class': 'temp fact__temp fact__temp_size_s'})

			def temperature_now(divs):
				for div in divs:
					output_now = div.find('span', attrs={'class': 'temp__value'}).text
					return "Температура чичас: " + output_now + ' C°'

			divs = soup.find_all('div', attrs={'class': 'link__feelings fact__feelings'})

			def temperature_feels(divs):
				for div in divs:
					output_feels = div.find('span', attrs={'class': 'temp__value'}).text
					return "Ощущается как: " + output_feels + ' C°'

			response = str(temperature_now(divs)) + '\n' + str(temperature_feels(divs))
			reply_text = response

			bot.send_message(
				chat_id=update.effective_message.chat_id,
				text=reply_text,
			)
			

def main():
	print('Start')
	scarlet_bot = Bot(
		token=TG_TOKEN,
		base_url='https://telegg.ru/orig/bot',
	)
	updater = Updater(
		bot=scarlet_bot
	)
	handler = MessageHandler(Filters.all, message_handler)
	updater.dispatcher.add_handler(handler)

	updater.start_polling()
	updater.idle()
	print('Finish')


if __name__ == '__main__':
	main()
