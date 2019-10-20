from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters


TG_TOKEN = ''


def message_handler(bot: Bot, update: Update):
	user = update.effective_user
	if user:
		name = user.first_name
	else:
		name = 'анонимыч'
	text = update.effective_message.text
	reply_text = f'Ну здарова {name}\n\n{text}'

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
