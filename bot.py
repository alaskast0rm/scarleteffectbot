from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import requests
from bs4 import BeautifulSoup as bs

TG_TOKEN = '968188661:AAEF4JBqD5OzPDK9I2LfTeQp-Jlr_Zd37u4'


def message_handler(bot: Bot, update: Update):
	user = update.effective_user
	if user:
		name = user.first_name
	else:
		name = 'анонимыч'
	text = update.effective_message.text
	reply_text = f'Ну здарова {name}\n\n{text}'

	if '/$' in text:
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
