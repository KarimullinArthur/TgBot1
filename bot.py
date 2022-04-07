import telebot
import sqlite3
import json
import ast
import markup 
import texts
from config import *

bot = telebot.TeleBot(TOKEN)

conn = sqlite3.connect('data.db', check_same_thread=False)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY);""")

@bot.message_handler(commands='start')
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,'Дарова',reply_markup=markup.menu)

    global conn
    global cur

    int(chat_id)
    cur.execute("INSERT OR IGNORE INTO users(id) VALUES(?)",(chat_id,))
    conn.commit()

@bot.message_handler(content_types='text')
def menu(message):
    chat_id = message.chat.id
    text = message.text

    if text == "Об авторе":
        bot.send_message(chat_id,texts.about,disable_web_page_preview=True,reply_markup=markup.menuIn)

    elif text == "Привет":
        bot.send_message(chat_id,'Hi')

    elif text == "Функции":
        msg = bot.send_message(chat_id,text,reply_markup=markup.func)
        bot.register_next_step_handler(msg,funcMenu)

def funcMenu(message):
    chat_id = message.chat.id
    text = message.text

    if text == "Мой ID":
        msg = bot.send_message(chat_id,chat_id)
        bot.register_next_step_handler(msg,funcMenu)

    elif text == "Узнать @username по ID":
        msg = bot.send_message(chat_id,f"@{message.from_user.username}")
        userName = bot.get_chat(chat_id)

        #a = str(a)

        #userName = json.dumps(a)
        userName = str(userName)
        userName.replace("\'",'\"')

        userName = json.dumps(userName)

        userName = json.loads(userName)
        #userName = ast.literal_eval(userName)

        print(userName)
        print(type(userName))

        bot.send_message(chat_id,userName['username'])
        bot.register_next_step_handler(msg,funcMenu)

    elif text == "Назад":
        msg = bot.send_message(chat_id,text,reply_markup=markup.menu)
        bot.register_next_step_handler(msg,menu)
print('Run!')
bot.infinity_polling()
