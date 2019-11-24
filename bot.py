from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import requests
from bs4 import BeautifulSoup as bs
import random
import telegram
import datetime

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
		print(text)
		bot.send_photo(
			chat_id=update.effective_message.chat_id,
			photo=reply_text,

		)

	if '/r' in text:
		number_1 = 0
		number_2 = 0

		if '/r1' in text:
			number_1 = 3
			number_2 = 1

		elif '/r2' in text:
			number_1 = 4
			number_2 = 2

		if number_1 != 0 and number_2 != 0:
			now = datetime.datetime.now()
			year = str(now.year)
			now_year = year[2:]
			now_month = now.month
			now_day = now.day
			day = str(text[4:-3])
			month = str(text.split('.')[-1])

			if len(text) > 3:
				url = f"http://sd.studga.ru/d/oneday?fac=3&flow=188&grp=2&lsubgrp={number_1}&esubgrp={number_2}&ofdate=2019-{month}-{day}"
				date = f'{day}.{month}.{now_year}'

			else:
				url = f"http://sd.studga.ru/d/oneday?fac=3&flow=188&grp=2&lsubgrp={number_1}&esubgrp={number_2}&ofdate=2019-{now_month}-{now_day}"
				date = f'{now_day}.{now_month}.{now_year}'

			if len(day) == 2 and len(month) == 2 or (len(str(now_day)) == 2 and len(str(now_month))) == 2:
				session = requests.Session()
				request = session.get(url, headers=head)

				if request.status_code == 200:
					soup = bs(request.content, 'html.parser')
					tbody = soup.find_all('tr', {'style': "background-color: #FFFFFF; "})
					counter = 1
					output = ''
					output_table_day_of_the_week = soup.find('center').find_all('b')[-1].text
					date_and_day_of_the_week = '📅 ' + date + ' - ' + output_table_day_of_the_week + '\n'

					for table in tbody:
						output_table_para = table.find('td', {
							'style': "width: 70px; border: 1px solid #000000; text-align: center;"}).find('strong').text

						output_table_time = table.find('td', {
							'style': "width: 70px; border: 1px solid #000000; text-align: center;"}).find('small').text

						output_table_subject = table.find('td', {'style': "border: 1px solid #000000"}).find('b').text

						output_table_teacher = table.find('td', {'style': "border: 1px solid #000000"}).find('small').text

						output_table_aud = table.find('td', {'style': "border: 1px solid #000000"}).find('i').text

						output_table_kind = soup.find_all('i')[counter].text

						counter += 2

						output += '\n◽️ ' + output_table_para + '\n🕙 ' + output_table_time + \
								  '\n📖 ' + output_table_subject + '\n👤 ' + output_table_teacher \
								  + '\n🏢 ' + output_table_aud + '\n⚪️ ' + output_table_kind + '\n\n\n'

					reply_text = date_and_day_of_the_week + output

					if len(output) == 0:
						reserve_responce = soup.find('table', {'class': 'shadow'}).find('strong').text
						reply_text = date_and_day_of_the_week + reserve_responce
						
						if type(reserve_responce) == "NoneType":
							reply_text = date_and_day_of_the_week + '\n 😌 Пар нет, отдыхаем !'
							
			else:
				reply_text = "❌ Неправильный ввод !"

		else:
			reply_text = "❌ Неправильный ввод !"

		bot.send_message(
			chat_id=update.effective_message.chat_id,
			text=reply_text,
		)

	if '/bc' in text:
		photo_url = "https://www.tradingview.com/x/2D4tS4y6"
		bot.send_photo(
			timeout=10,
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
			# divs_time_now = soup.find_all('div', attrs={'class': 'fact__time-yesterday-wrap'})
			#
			# def time_now(divs_time_now):
			# 	for div in divs_time_now:
			# 		output_time_now = div.find('time', attrs={'class': 'time fact__time'}).text
			# 		return output_time_now + '\n'

			divs_now = soup.find_all('div', attrs={'class': 'temp fact__temp fact__temp_size_s'})

			def temperature_now(divs_now):
				for div in divs_now:
					output_now = div.find('span', attrs={'class': 'temp__value'}).text
					return "Температура: " + output_now + '°\n'

			divs_feels = soup.find_all('div', attrs={'class': 'link__feelings fact__feelings'})

			def temperature_feels(divs_feels):
				for div in divs_feels:
					output_feels = div.find('span', attrs={'class': 'temp__value'}).text
					return "Ощущается как: " + output_feels + '°\n'

			divs_yesterday_temperature = soup.find_all('dl', attrs={
				'class': 'term term_orient_h term_size_wide fact__yesterday'})

			def yesterday_temperature(divs_yesterday_temperature):
				for div in divs_yesterday_temperature:
					output_yesterday_temperature = div     .find('span', attrs={'class': 'temp__value'}).text
					return '\nВчера в это время: ' + output_yesterday_temperature + '°\n'

			divs_condition = soup.find('div', {'class': "link__feelings fact__feelings"}).find('div').text

			response = str(temperature_now(divs_now)) + str(
				temperature_feels(divs_feels)) + str(divs_condition) + str(yesterday_temperature(divs_yesterday_temperature))
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
