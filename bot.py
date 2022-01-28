import random
import requests
import telebot
from telebot import types

bot = telebot.TeleBot('5287784518:AAE9ZH8p6L5MxfPO0eUMPy11Z9y-_hQQoug')




@bot.message_handler(commands=["start"])
def start(m, res=False):
    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')
    text = response.content.decode('cp1251')
    with open('russian.txt', 'wb') as ru:
        ru.write(text.encode('utf-8'))
    text = text.split('\n')
    text1 = []
    for n in text:
        if len(n) < 3:
            continue
        if n[-3:] in ('ого', 'его', 'ему', 'ому', 'или', 'ова', 'ева', 'ими', 'еми', 'ыми', 'ами', 'ала', 'ела', 'ила'):
            continue
        if n[-2:] in (
        'ая', 'ое', 'ую', 'юю', 'ою', 'им', 'ку', 'ся', 'сь', 'те', 'ых', 'их', 'ла', 'ов', 'ев', 'ив', 'ыв',
        'яв', 'ув', 'ые', 'ие', 'ее', 'ом', 'ем', 'аю', 'ею', 'ам', 'ью', 'ию', 'ым', 'ей', 'ой'):
            continue
        else:
            text1.append(n)

    def word_list():
        a = random.sample(text1, 12)
        for i in range(12):
            print(a[i])
    bot.send_message(m.chat.id, random.sample(text1, 1))
    bot.send_message(m.chat.id, random.sample(text1, 1))
    bot.send_message(m.chat.id, random.sample(text1, 1))
    bot.send_message(m.chat.id, random.sample(text1, 1))
    bot.send_message(m.chat.id, random.sample(text1, 1))
    bot.send_message(m.chat.id, random.sample(text1, 1))
    bot.send_message(m.chat.id, random.sample(text1, 1))
    bot.send_message(m.chat.id, random.sample(text1, 1))
    bot.send_message(m.chat.id, random.sample(text1, 1))
    bot.send_message(m.chat.id, '/start')
bot.polling(none_stop=True, interval=0)