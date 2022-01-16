import telebot
from telebot import types

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row('Привет',"Об авторе")
menu.row('Функции')

func = types.ReplyKeyboardMarkup(resize_keyboard=True)
func.row("Мой ID")
func.row("Назад")

menuIn = types.InlineKeyboardMarkup()
mastodon = types.InlineKeyboardButton(text="Mastodon", url="https://mastodon.ml/web/accounts/107458021118240568")
gitHub = types.InlineKeyboardButton(text="GitHub", url="https://Github.com/KarimullinArthur")
matrix = types.InlineKeyboardButton(text='Matrix', url='https://matrix.to/#/@karimullin-arthur:matrix.org')
menuIn.add(gitHub)
menuIn.add(mastodon,matrix)