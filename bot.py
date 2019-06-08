from telegram.ext import Updater, CommandHandler


def start(bot, update):
    update.message.reply_text('Welcome bro')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('800961762:AAEDkucfaCgesFDizuA9IhReHZL2Xkcaz_k')

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()

print("bot started")