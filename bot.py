from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import requests
from bs4 import BeautifulSoup as bs
import random
import datetime
import re
import csv
import numpy as np
import pandas as pd
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings(action='once')





TG_TOKEN = "968188661:AAHL7cMXXsej4c2KaNIF0llikNoSOWyTzRg"
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

	if 'ga' in text:
		large = 22
		med = 16
		small = 12
		params = {'axes.titlesize': large,
				  'legend.fontsize': med,
				  'figure.figsize': (16, 10),
				  'axes.labelsize': med,
				  'axes.titlesize': med,
				  'xtick.labelsize': med,
				  'ytick.labelsize': med,
				  'figure.titlesize': large}
		plt.rcParams.update(params)
		plt.style.use('seaborn-whitegrid')
		sns.set_style("white")

		# Version
		print(mpl.__version__)  # > 3.0.0
		print(sns.__version__)  # > 0.9.0

		# rng = np.arange(50)
		# rnd = np.random.randint(0, 10, size=(3, rng.size))
		# yrs = 2000 + rng
		#
		# fig, ax = plt.subplots(figsize=(5, 3))
		# ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
		# ax.set_title('Combined debt growth over time')
		# ax.legend(loc='upper left')
		# ax.set_ylabel('Total debt')
		# ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
		# fig.tight_layout()
		# x = np.arange(0, 5, 0.1)
		# y = x*2 + 2 - 20 + (1 / 120)
		# plt.figure(dpi=200)
		# plt.plot(x, y)
		# plt.xlabel('Сашенька хуй саси')
		# plt.ylabel('хихихихи')
		# plt.savefig('www.png')
		# #a = plt.show()
		# print('a')
		# photo = open("www.png", "rb")
		# Import Data
		df = pd.read_csv('dataa.csv')

		print(df)

		# Draw Plot
		plt.figure(figsize=(16, 10), dpi=80)
		print('figure')
		plt.plot('date', 'low', data=df, color='red')

		print('Draw')

		# Decoration
		plt.ylim(50, 750)
		xtick_location = df.index.tolist()[::366]
		xtick_labels = [x[:4] for x in df.date.tolist()[::366]]
		plt.xticks(ticks=xtick_location, labels=xtick_labels, rotation=0, fontsize=12, horizontalalignment='center',
				   alpha=.7)
		plt.yticks(fontsize=12, alpha=.7)
		plt.title("Air Passengers Traffic (1949 - 1969)", fontsize=22)
		plt.grid(axis='both', alpha=.3)

		print('Decoration')

		# Remove borders
		plt.gca().spines["top"].set_alpha(0.0)
		print('top')
		plt.gca().spines["bottom"].set_alpha(0.3)
		print('bottom')
		plt.gca().spines["right"].set_alpha(0.0)
		print('right')
		plt.gca().spines["left"].set_alpha(0.3)
		print('left')
		plt.savefig('ww4w.png')

		print('Save')

		photo = open('ww4w.png', 'rb')

		print('Open')

		bot.send_photo(
			chat_id=update.effective_message.chat_id,
			photo=photo,

		)
		print("Send")


	if '/dol' in text:
		url = 'http://www.profinance.ru/currency_usd.asp'
		sesion = requests.Session()
		request = sesion.get(url, headers=head)

		if request.status_code == 200:
			soup = bs(request.content, 'html.parser')

			td_cb = soup.find_all('td', attrs={'align': "center", 'class': 'cell'})

			name_cb = td_cb[0].text
			from_date_cb = td_cb[1].text
			on_date_cb = td_cb[2].text
			value_from_date_cb = td_cb[5].text
			value_on_date_cb = td_cb[6].text
			name_forex = td_cb[-6].text
			date_forex = td_cb[-5].text
			name_moscow = td_cb[-4].text
			date_moscow = td_cb[-3].text
			value_forex = td_cb[-2].text
			value_moscow = td_cb[-1].text
			print(value_moscow)

			reply_text = name_cb + from_date_cb + value_from_date_cb + on_date_cb + value_on_date_cb + name_forex + '\n' + date_forex + '\n' + value_forex + '\n' + name_moscow + '\n' + date_moscow + '\n' + value_moscow
			print(reply_text)

		else:
			reply_text = "Ошибка с подклюючением."

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

		else:
			reply_text = "Ошибка с подклюючением."

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

		else:
			reply_text = "Ошибка с подклюючением."

		bot.send_message(
			chat_id=update.effective_message.chat_id,
			text=reply_text,
		)

	global global_msg

	if '/cat' in text:
		url = 'https://random.cat/view/'
		number = random.randint(1, 1500)
		reply_text = url + str(number)
		msg = bot.send_photo(
			chat_id=update.effective_message.chat_id,
			photo=reply_text,

		)
		global_msg = msg

	if '/delete' in text:
		bot.delete_message(
			chat_id=global_msg.chat_id,
			message_id=global_msg.message_id,
		)

	if '/veven' in text:
		print('veven')

		bot.send_message(
			chat_id=update.effective_message.chat_id,
			text="Пожалуйста, подождите пару секунд.",
		)

		url = "1https://studga.wohlnet.ru/d/full?fac=3&flow=188&grp=2&lsubgrp=3&esubgrp=1"
		headers = head
		session = requests.Session()
		request = session.get(url, headers=headers)
		counter = 7
		pattern_day = r'\s[0-3][0-9].'
		pattern_month = r'.[0-1][0-9]'
		check_day = re.findall(pattern_day, text)
		check_month = re.findall(pattern_month, text)

		if check_day and check_month:
			if len(text) == 12:
				try:
					day = int(str(check_day).split("'")[1].split('.')[0])
					month = int(str(check_month).split('.')[-1].split("'")[0])
					year = 2020
				except:
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=" ❌ Неправильный ввод !\n" + "✅ Пример правильного ввода:\n" + "		/seven 02.12"
					)

				if day > 31 or month > 12 or day == 0 or month == 0:

					text = " ❌ Неправильный ввод !\n" + "✅ Пример правильного ввода:\n" + "		/seven 02.12"
			else:
				text = " ❌ Неправильный ввод !\n" + "✅ Пример правильного ввода:\n" + "		/seven 02.12"
				bot.send_message(
					chat_id=update.effective_message.chat_id,
					text=text
				)
		elif text == '/veven@scarlet_effect_bot' or text == '/veven':
			if request.status_code == 200:
				soup = bs(request.content, 'html.parser')
				try:
					body_today = soup.find('tr', attrs={'style': "height: 60px;", 'class': "tr_today"})
					date = body_today.find('a')['href']
				except AttributeError:
					body_tomorrow = soup.find('tr', attrs={'style': "height: 60px;", 'class': "tr_tomorrow"})
					date = body_tomorrow.find('a')['href']
				new_date = date.split('=')[-1]
				day = new_date[8:]
				month = int(new_date[5:7])
				year = int(new_date[:4])
				if day[0] == 0:
					day = int(day[1])
				else:
					day = int(day)

			else:
				bot.send_message(
					chat_id=update.effective_message.chat_id,
					text="Ошибка с подключением."
				)

		else:
			bot.send_message(
				chat_id=update.effective_message.chat_id,
				text=" ❌ Неправильный ввод !\n" + "✅ Пример правильного ввода:\n" + "		/seven 02.12"
			)

		def receiving_data(year, month, day):
			if len(str(day)) == 1:
				day = '0' + str(day)

			if len(str(month)) == 1:
				month = '0' + str(month)

			try:

				url = f'https://studga.wohlnet.ru/d/oneday?fac=3&flow=188&grp=2&lsubgrp=3&esubgrp=1&ofdate={year}-{month}-{day}'
				session = requests.Session()
				request = session.get(url, headers=head)

				if request.status_code == 200:

					soup = bs(request.content, 'html.parser')
					tbody = soup.find_all('tr', {'style': "background-color: #FFFFFF; "})
					counter = 1
					output = ''
					output_table_day_of_the_week = soup.find('center').find_all('b')[-1].text
					date_and_day_of_the_week = '📅 ' + str(day) + '.' + str(month) + '.' + str(
						year) + ' - ' + output_table_day_of_the_week + '\n'

					for table in tbody:
						output_table_para = table.find('td', {
							'style': "width: 70px; border: 1px solid #000000; text-align: center;"}).find('strong').text

						output_table_time = table.find('td', {
							'style': "width: 70px; border: 1px solid #000000; text-align: center;"}).find('small').text

						output_table_subject = table.find('td', {'style': "border: 1px solid #000000"}).find('b').text

						output_table_teacher = table.find('td', {'style': "border: 1px solid #000000"}).find(
							'small').text

						output_table_aud = table.find('td', {'style': "border: 1px solid #000000"}).find('i').text

						output_table_kind = soup.find_all('i')[counter].text

						counter += 2

						output += '\n◽️ ' + output_table_para + '\n🕙 ' + output_table_time + \
								  '\n📖 ' + output_table_subject + '\n👤 ' + output_table_teacher \
								  + '\n🏢 ' + output_table_aud + '\n⚪️ ' + output_table_kind + '\n\n'
					if len(output) == 0:
						output = 'Пар нет, отдыхаем '

					reply_text = date_and_day_of_the_week + output
					return reply_text

			except:
				bot.send_message(
					chat_id=update.effective_message.chat_id,
					text="Ошибка с подключением."
				)

		if day > 31 or month > 12:
			bot.send_message(
				chat_id=update.effective_message.chat_id,
				text=" ❌ Неправильный ввод !\n" + "✅ Пример правильного ввода:\n" +"		/seven 02.12"
			)
		else:

			if month == 12:
				for i in range(counter):
					if day > 31:
						month = 1
						day = 1
						year += 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 11:
				for i in range(counter):
					if day > 30:
						month = 12
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 10:
				for i in range(counter):
					if day > 31:
						month = 11
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 9:
				for i in range(counter):
					if day > 30:
						month = 10
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 8:
				for i in range(counter):
					if day > 31:
						month = 9
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 7:
				for i in range(counter):
					if day > 31:
						month = 8
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 6:
				for i in range(counter):
					if day > 30:
						month = 7
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 5:
				for i in range(counter):
					if day > 31:
						month = 6
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 4:
				for i in range(counter):
					if day > 30:
						month = 5
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 3:
				for i in range(counter):
					if day > 31:
						month = 4
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 2:
				for i in range(counter):
					if day > 29:
						month = 3
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

			if month == 1:
				for i in range(counter):
					if day > 31:
						month = 2
						day = 1
						continue
					else:
						reply_text = receiving_data(year, month, day)
						day += 1
						counter -= 1
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text=reply_text + "\n"
					)

	if '/r' in text:
		number_1 = 0
		number_2 = 0
		now = datetime.datetime.now()
		year = str(now.year)
		now_year = year[2:]
		now_month = str(now.month)
		now_day = str(now.day)
		now_time = str(now.time())

		if '/r1' in text:
			number_1 = 3
			number_2 = 1

		if '/r2' in text:
			number_1 = 4
			number_2 = 2

		if number_1 != 0 and number_2 != 0:
			if len(text) > 3 and '@scarlet_effect_bot' not in text:
				day = str(text.split(' ')[1].split('.')[0])
				month = str(text.split(' ')[1].split('.')[1])
				pattern = r"[a-zA_Z_]"
				check_day = re.findall(pattern, day)
				check_month = re.findall(pattern, month)

				if not check_day and not check_month:
					if len(day) == 1:
						zero_plus_day = '0' + day
						day = zero_plus_day
					if len(month) == 1:
						zero_plus_month = '0' + month
						month = zero_plus_month

					url = f"http://sd.studga.ru/d/oneday?fac=3&flow=188&grp=2&lsubgrp={number_1}&esubgrp={number_2}&ofdate=2020-{month}-{day}"
					date = f'{day}.{month}.{now_year}'

				else:
					bot.send_message(
						chat_id=update.effective_message.chat_id,
						text='❌ Неправильный ввод !' + '\nВремя на сервере: ' + now_time,
					)

			if text == "/r2" or text == "/r1" or text == "/r2@scarlet_effect_bot" or text == "/r1@scarlet_effect_bot":
				url = f"http://sd.studga.ru/d/oneday?fac=3&flow=188&grp=2&lsubgrp={number_1}&esubgrp={number_2}&ofdate=2020-{now_month}-{now_day}"
				date = f'{now_day}.{now_month}.{now_year}'

				if len(now_day) == 1:
					now_day_with_zero = '0' + now_day
					now_day = now_day_with_zero
					date = f'{now_day}.{now_month}.{now_year}'

				if len(now_month) == 1:
					now_month_with_zero = '0' + now_month
					now_month = now_month_with_zero
					date = f'{now_day}.{now_month}.{now_year}'

			if (len(now_day) == 2) or (len(now_month) == 2) or (len(day) == 2 and len(month) == 2):
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
								  + '\n🏢 ' + output_table_aud + '\n⚪️ ' + output_table_kind + '\n\n'

					reply_text = date_and_day_of_the_week + output

					if len(output) == 0:
						reserve_responce = soup.find('table', {'class': 'shadow'}).find('strong').text
						reply_text = date_and_day_of_the_week + reserve_responce
						if "Имеется новое расписание, занятия ещё не начались" in reserve_responce:
							reply_text = "❌ Неправильный ввод !"
				else:
					reply_text = "Ошибка с подклюючением."
			else:
				reply_text = "❌ Неправильный ввод !"

		else:
			reply_text = "❌ Неправильный ввод !"

		if reply_text == "❌ Неправильный ввод !" or reply_text == "Ошибка с подключением.":
			bot.send_message(
				chat_id=update.effective_message.chat_id,
				text=reply_text + '\nВремя на сервере: ' + now_time,
				reply_to_message_id=update.effective_message.message_id,
			)
		else:
			msg = bot.send_message(
				chat_id=update.effective_message.chat_id,
				text=reply_text + '\nВремя на сервере: ' + now_time,
				reply_to_message_id=update.effective_message.message_id,
			)
			bot.pin_chat_message(
				chat_id=msg.chat_id,
				message_id=msg.message_id,
			)

	if '/bc' in text:
		photo_url = "https://www.tradingview.com/x/2D4tS4y6"
		bot.send_photo(
			timeout=10,
			chat_id=update.effective_message.chat_id,
			photo=photo_url,
		)

	if '/weather' in text:
		headers = head
		url_time = "https://voshod-solnca.ru/time/%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%B0"
		session_time = requests.Session()
		request_time = session_time.get(url_time, headers=headers)
		soup_time = bs(request_time.content, 'html.parser')
		body_time = soup_time.find('span', attrs={'id': "exact-time0"}).text
		moscow_time = 'Время: ' + body_time

		url = "https://yandex.ru/pogoda/moscow?lat=55.85489273&lon=37.47623444&name=%D0%BC%D0%B5%D1%82%D1%80%D0%BE%20%D0%A0%D0%B5%D1%87%D0%BD%D0%BE%D0%B9%20%D0%B2%D0%BE%D0%BA%D0%B7%D0%B0%D0%BB%2C%20%D0%97%D0%B0%D0%BC%D0%BE%D1%81%D0%BA%D0%B2%D0%BE%D1%80%D0%B5%D1%86%D0%BA%D0%B0%D1%8F%20%D0%BB%D0%B8%D0%BD%D0%B8%D1%8F%2C%20%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0&kind=metro"
		session = requests.Session()
		request = session.get(url, headers=headers)

		if request.status_code == 200:
			soup = bs(request.content, 'html.parser')
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

			def yesterday_temperature():
				output_yesterday_temperature = soup.find('div', attrs={'class': 'fact__time-yesterday-wrap'}).find('span', attrs={'class': 'temp__value'}).text
				return '\nВчера в это время: ' + output_yesterday_temperature + '°\n'

			divs_condition = soup.find('div', {'class': "link__feelings fact__feelings"}).find('div').text
			
			if divs_condition == 'Дождь со снегом':
				emoji = ' 🌧🌨'
			elif divs_condition == 'Небольшой дождь' or divs_condition == 'Дождь':
				emoji = ' 🌧'
			elif divs_condition == 'Пасмурно':
				emoji = ' ☁️'
			elif divs_condition == 'Снег' or divs_condition == 'Небольшой снег':
				emoji = ' 🌨'
			elif divs_condition == 'Облачно':
				emoji = ' ⛅️'
			elif divs_condition == 'Солнечно' or divs_condition == 'Ясно':
				emoji = ' ☀️'
			elif divs_condition == 'Облачно с прояснениями':
				emoji = ' 🌥'
			else:
				emoji = ''

			response = str(temperature_now(divs_now)) + str(
				temperature_feels(divs_feels)) + str(divs_condition) + emoji + str(yesterday_temperature()) + str(moscow_time)
			reply_text = response

		else:
			reply_text = "Ошибка с подклюючением."

		bot.send_message(
			chat_id=update.effective_message.chat_id,
			text=reply_text,
		)


def main():
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


if __name__ == '__main__':
	main()
