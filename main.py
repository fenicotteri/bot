import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot('6283001284:AAHq1hTf2FEGor5C0h1JHqnuoYnncGEZ9Rc')


def get_txt(link):
    url = link
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    quotes = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-6 YYrds')
    txt = ""
    for q in quotes:
        txt += q.text
    count = 0
    for letter in txt:
        if letter.isupper():
            txt = txt[:count] + "\n" + txt[count:]
            count += 1
        count += 1
    return txt


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("INSTASAMKA")
    btn2 = types.KeyboardButton('Oxxxymiron')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "Выбери своего персонажика", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == "INSTASAMKA":
        bt1 = types.KeyboardButton("👌👈 И ЧТОЭ")
        bt2 = types.KeyboardButton("К списку исполнителей")
        markup.add(bt1, bt2)
        bot.send_message(message.from_user.id, "Выбери тречок", reply_markup=markup)

    elif message.text == "Oxxxymiron":
        bt1 = types.KeyboardButton("🥶 ДО ЗИМЫ")
        bt2 = types.KeyboardButton("К списку исполнителей")
        markup.add(bt1, bt2)
        bot.send_message(message.from_user.id, "Выбери тречок", reply_markup=markup)

    elif message.text == "🥶 ДО ЗИМЫ":
        txt = get_txt('https://genius.com/Oxxxymiron-until-winter-lyrics')
        bt2 = types.KeyboardButton("К списку исполнителей")
        markup.add(bt2)
        bot.send_message(message.from_user.id, txt, reply_markup=markup)

    elif message.text == "👌👈 И ЧТОЭ":
        txt = get_txt('https://genius.com/Instasamka-and-whate-lyrics')
        bt2 = types.KeyboardButton("К списку исполнителей")
        markup.add(bt2)
        bot.send_message(message.from_user.id, txt, reply_markup=markup)

    elif message.text == "К списку исполнителей":
        btn1 = types.KeyboardButton("INSTASAMKA")
        btn2 = types.KeyboardButton('Oxxxymiron')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Выбери своего персонажика", reply_markup=markup)


bot.polling(none_stop=True, interval=0)
