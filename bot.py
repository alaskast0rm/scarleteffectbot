from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import requests
from bs4 import BeautifulSoup as bs
import random
from selenium import webdriver

TG_TOKEN = '968188661:AAEF4JBqD5OzPDK9I2LfTeQp-Jlr_Zd37u4'


def message_handler(bot: Bot, update: Update):
	user = update.effective_user
	if user:
		name = user.first_name
	else:
		name = 'анонимыч'
	text = update.effective_message.text
	reply_text = f'Ну здарова {name}\n\n{text}'


	if '/dol' in text:
		print('zhopa')
		headers = {'accept': '*/*',
				   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

		url = 'https://www.banki.ru/products/currency/usd/'

		# def bank(url, headers):
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
	if '/hh' in text:
		url = 'https://hh.ru/search/vacancy?only_with_salary=false&clusters=true&area=1&enable_snippets=true&salary=&st=searchVacancy&text=Python+junior'

		headers = {'accept': '*/*',
				   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

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
				# print(f'{counter})', divka)
				# divkaa = str(divka)
				# print(type(divkaa))
				# divss = str(divs)
				# print(type(divs))
				mod_divka_https = divka_https['href']

				def result(divka):
					return '\n'.join(str(divka) for i in range(1))

				def result_https(mod_divka_https):
					return '\n'.join(str(mod_divka_https) for i in range(1))

				response += f'{counter}) ' + str(result(divka)) + f"\n{result_https(mod_divka_https)}\n"
			reply_text = response
	# print(response)

	if '/cat' in text:
		url = 'https://random.cat/view/'
		number = random.randint(1, 1500)
		reply_text = url + str(number)

	bot.send_message(
		chat_id=update.effective_message.chat_id,
		text=reply_text,
	)
	if '/bc' in text:
		
		bot.send_photo(
			chat_id=udate.effective_message.chat_id,
			text="https://www.tradingview.com/x/2D4tS4y6",
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
