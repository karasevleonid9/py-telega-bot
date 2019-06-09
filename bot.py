import json
import pymongo
from telegram.ext import Updater, CommandHandler

# loading config
with open('config.json', 'r', encoding='utf8') as f:
	conf = json.load(f)

#loading db seed
with open('database/seed.json', 'r', encoding='utf8') as f:
	seed = json.load(f)

# mongodb connection
client = pymongo.MongoClient(conf["mongodb"])
db = client.test

def startHandler(bot, update):
	update.message.reply_text(seed['maintenance_msg'])

def helpHandler(bot, update)
	update.message.reply_text(seed['help'])

def main():
	updaters = []
	for token in conf['bots']:
		updater = Updater(token)
		updater.dispatcher.add_handler(CommandHandler('start', startHandler))
		updater.dispatcher.add_handler(CommandHandler('help', helpHandler))
		updaters.append(updater)

	for updater in updaters:
		updater.start_polling()
		#updater.idle()

if __name__ == '__main__':
    main()