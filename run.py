
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from climate.callbacks import (
    start,select_location,contact,climate
)

TOKEN = os.environ['TOKEN']

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(MessageHandler(Filters.text('hozirgi ob-havo'), climate))
    dp.add_handler(MessageHandler(Filters.text('🌆Hududni tanlash'), select_location))
    dp.add_handler(MessageHandler(Filters.text('☎️Aloqa'),contact ))
    dp.add_handler(MessageHandler(Filters.text('Andijon'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Namangan'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Qashqadaryo'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Toshkent'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Fargona'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Sirdaryo'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Termiz'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Navoiy'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Urganch'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Samarqand'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Jizzax'), climate ))
    dp.add_handler(MessageHandler(Filters.text('Buxoro'), climate ))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
