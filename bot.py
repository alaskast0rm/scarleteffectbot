from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
import random
import datetime
import time

TG_TOKEN = '968188661:AAEF4JBqD5OzPDK9I2LfTeQp-Jlr_Zd37u4'


def message_handler(bot: Bot, update: Update):
	user = update.effective_user
	if user:
		name = user.first_name
	else:
		name = 'анонимыч'
	text = update.effective_message.text
	if '/go' in text:
		local_time = datetime.datetime.now()
		for_server_time = datetime.timedelta(hours=3)
		server_time = local_time + for_server_time
		aha = str(server_time)
		split_date = aha.split('-')[0]
		sd = int(split_date)
		split_date1 = aha.split('-')[1]
		sd1 = int(split_date1)
		split_date2 = aha.split('-')[2]
		sd2_0 = split_date2
		sd2_1 = sd2_0.split(' ')[0]
		sd2_2 = int(sd2_1)
		target = datetime.datetime(sd, sd1, sd2_2, 8, 0, 10)

		difference = target - server_time
		seconds = difference.seconds
		time.sleep(seconds)

			#if '/me' in text:
				#return 0
	#if 'саша' or 'санек' or 'саня' in text:
		#sasha = 'Ну да это санька сашка саня\n'
	#else:
		#sasha = ''
		#vstavochka = ['ну да как всегда смешно', 'ахахахах смешно да', 'хахахаха котики смешно']
		#random_vstavochka = random.choice(vstavochka)
		#reply_text = f'{random_vstavochka} -->{name}\n\n{text}\n'
		reply_text = ("Доброе утро кролики! :)\n\n"
		    "Желаю утра доброго\n"
                      "И солнечных лучей,\n"
                      "Улыбок притягательных,\n"
                      "Приятных мелочей.\n\n"
                      "Пусть настроенье доброе\n"
                      "Весь день не подведет,\n"
                      "Заставит быстро двигаться\n"
                      "Лишь вверх и лишь вперед.")
		bot.send_message(
			chat_id=update.effective_message.chat_id,
			text=reply_text,
		)

	
	



def main():
	print('Start')
	scarlet_bot = Bot(
		token=TG_TOKEN,
		#base_url='https://telegg.ru/orig/bot',
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
