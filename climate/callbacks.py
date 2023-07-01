from telegram.ext import  CallbackContext
from telegram import Update,KeyboardButton,ReplyKeyboardMarkup
import requests
import datetime
from pprint import pprint



TOKEN= "6286747512:AAE80UkdTFBY0ko1PlmBMzim8TnZh-gULAI"
def start(update: Update, context: CallbackContext):
    chat = update.message.chat.id
   

    # btn1 = KeyboardButton('hozirgi ob-havo')
    btn2 = KeyboardButton('🌆Hududni tanlash')
    btn3 = KeyboardButton('☎️Aloqa')
   
    reply_keyboard =[
                     [btn2],
                     [btn3]
                     ]

    context.bot.sendMessage(chat_id=chat,
                             text= 'Assalomu aleykum, botimizga xush kelibsiz \n biz siz tanladan hudud boyicha ayni \n vaqtdagi ob-havo malumotlarini yetkazanim',
                             reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard,resize_keyboard=True))
def contact(update:Update,context:CallbackContext):
    
    chat = update.message.chat.id
   

  

    context.bot.sendMessage(chat_id=chat,
    text= "Assalomu alaykum, Ob-havo botiga hush kelibsiz \n 🚀 Bu bot orqali O'\zbekistonnig barcha hududlaridagi ob-havo ma'lumotini ko'rishingiz mumkin. Bot sizga foyda keltirsa biz hursand bo'lamiz. \n Bot orqali siz, hududingizdagi  ob-havo ma'lumotni bilishingiz mumkin \n 📩 Takliflaringiz bo'lsa @softlyuz ga yuborishingiz mumkin \n Qilgan ishlarimiz va foaliyatimiz haqida shu kanalda tanishish mumkin \n 👉 @softly_uz Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing"
    
    )

def climate (update:Update,context:CallbackContext):
    
    chat = update.message.chat.id

  

    #context.bot.sendMessage(chat_id=chat,
    sana = datetime.date.today()
    hudud = update.message.text
    # temp = response.json()['main']['temp']
    # pprint(temp)
    # text= f"""Bugun, {sana}
    
    # {hudud}
   

    # 🔹 Hozirgi ob-havo ma'lumoti
    
    # Temperatura: {temp} C°
    # Tuyuladi: 27 C°

    # ———

    # Bulutlar: 100%
    # Namlik: 31%
    # Shamol: 5.65 m/s
    # Bosim: 754 mm sim. ust.
    # Quyosh chiqishi: :40
    # Quyosh botishi: 19:46

    # Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing"""

    
    
    city = update.message.text
    url_for_weather = f'https://api.openweathermap.org/data/2.5/weather/'

    key = 'c0d5478f5b490a27149f56f39fbe7fd6'
    URL = url_for_weather
    params = {
            'q':city,
            'appid':key
        }
        
    response = requests.get(URL, params=params)
    #pprint(response.json())
    temp = (response.json()['main']['temp'] - 273.15)//1
    feels = (response.json()['main']['feels_like']-273.15)//1
    clouds = response.json()['clouds']['all']
    humidity = response.json()['main']['humidity']
    wind = response.json()['wind']['speed']
    sunrise = response.json()['sys']['sunrise']
    sunset = response.json()['sys']['sunset']
    text= f"""Bugun, {sana}
    
    {hudud}
   

    🔹 Hozirgi ob-havo ma'lumoti
    
    Temperatura: {temp} C°
    Tuyuladi: {feels} C°

    ———

    Bulutlar: {clouds}%
    Namlik: {humidity}%
    Shamol: {wind} m/s
    Quyosh chiqishi: :{sunrise}
    Quyosh botishi: {sunset}

    Foydali deb bilgan bo'lsangiz yaqinlaringizga ham ulashing"""
    bot = context.bot

    bot.sendMessage(chat, text)


def select_location(update: Update, context: CallbackContext):
    chat = update.message.chat.id
    first_name = update.message.chat.first_name
   

    btn1 = KeyboardButton('Andijon')
    btn2 = KeyboardButton('Namangan')
    btn3 = KeyboardButton('Qashqadaryo')
    btn4 = KeyboardButton('Toshkent')
    btn5 = KeyboardButton('Fargona')
    btn6 = KeyboardButton('Sirdaryo')
    btn7 = KeyboardButton('Termiz')
    btn8 = KeyboardButton('Navoiy')
    btn9 = KeyboardButton('Buxoro')
    btn10 = KeyboardButton('Urganch')
    btn11 = KeyboardButton('Jizzax')
    btn12 = KeyboardButton('Samarqand')
   
    reply_keyboard =[[btn1,btn2,btn3],
                     [btn4,btn5,btn6],
                     [btn7,btn8,btn9],
                     [btn10,btn11,btn12],
                     ]

    update.message.reply_html(
                            
                            text= f'Kerakli hududni tanlang  <b>{first_name}</b>',
                             reply_markup=ReplyKeyboardMarkup(keyboard=reply_keyboard,resize_keyboard=True))