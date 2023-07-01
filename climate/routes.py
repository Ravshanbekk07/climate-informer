from climate import app
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import os
from climate.callbacks import (
    select_location, contact, start, climate
)

from flask import request

TOKEN = os.environ['TOKEN']
bot = Bot(token=TOKEN)


@app.route('/webhook/', methods=['GET', 'POST'])
def main():
    dp = Dispatcher(bot, None, workers=0)
    update = Update.de_json(request.get_json(force=True), bot)

    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(MessageHandler(Filters.text('hozirgi ob-havo'), climate))
    dp.add_handler(MessageHandler(Filters.text(
        '🌆Hududni tanlash'), select_location))
    dp.add_handler(MessageHandler(Filters.text('☎️Aloqa'), contact))
    dp.add_handler(MessageHandler(Filters.text('Andijon'), climate))
    dp.add_handler(MessageHandler(Filters.text('Namangan'), climate))
    dp.add_handler(MessageHandler(Filters.text('Qashqadaryo'), climate))
    dp.add_handler(MessageHandler(Filters.text('Toshkent'), climate))
    dp.add_handler(MessageHandler(Filters.text('Fargona'), climate))
    dp.add_handler(MessageHandler(Filters.text('Sirdaryo'), climate))
    dp.add_handler(MessageHandler(Filters.text('Termiz'), climate))
    dp.add_handler(MessageHandler(Filters.text('Navoiy'), climate))
    dp.add_handler(MessageHandler(Filters.text('Urganch'), climate))
    dp.add_handler(MessageHandler(Filters.text('Samarqand'), climate))
    dp.add_handler(MessageHandler(Filters.text('Jizzax'), climate))
    dp.add_handler(MessageHandler(Filters.text('Buxoro'), climate))

    dp.process_update(update)
    return 'cool'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    bot.delete_webhook()
    s = bot.setWebhook('https://climateinformer7.pythonanywhere.com/webhook/')
    if s:
        return 'webhook setup ok'
    else:
        return 'webhook setup failed'
