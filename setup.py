import json
from telegram.ext import Updater, CommandHandler

with open('database/seed.json', 'r', encoding='utf8') as f:
        seed = json.load(f)
with open('config.json', 'r', encoding='utf8') as f:
        conf = json.load(f)

def start(bot, update):
    update.message.reply_text(seed['maintenance_msg'])

updaters = []
for token in conf['bots']:
        updater = Updater(token)
        updater.dispatcher.add_handler(CommandHandler('start', start))
        updaters.append(updater)


for updater in updaters:
        updater.start_polling()
        #updater.idle()
