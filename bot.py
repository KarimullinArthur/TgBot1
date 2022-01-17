import telebot
import markup 
import texts
from config import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands='start')
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,'Hello',reply_markup=markup.menu)

@bot.message_handler(content_types='text')
def menu(message):
    chat_id = message.chat.id
    text = message.text

    if text == "Об авторе":
        bot.send_message(chat_id,texts.about,reply_markup=markup.menuIn)

    if text == "Привет":
        bot.send_message(chat_id,'Hi')

    if text == "Функции":
        msg = bot.send_message(chat_id,text,reply_markup=markup.func)
        bot.register_next_step_handler(msg,funcMunu)

def funcMunu(message):
    chat_id = message.chat.id
    text = message.text

    if text == "Мой ID":
        msg = bot.send_message(chat_id,chat_id)
        bot.register_next_step_handler(msg,funcMunu)


    if text == "Назад":
        msg = bot.send_message(chat_id,text,reply_markup=markup.menu)
        bot.register_next_step_handler(msg,menu)
print('Run!')
bot.infinity_polling()