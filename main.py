import telebot
from telebot import types

from bot.message import MessageController

bot = telebot.TeleBot('6661071169:AAECn3_P2CWaWqYpwWdd4jvV_vCNoFGUkkU')
photo = r'C:\Users\Ученик\Downloads\спикер мен (2).jpg'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! Im One hundred n Bot. Im test Bot. I have commands: help, memes')

@bot.message_handler(commands=['help'])
def help(message):
    z = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Important info', url='https://www.youtube.com/watch?v=mrGefJndVhc')
    button2 = types.InlineKeyboardButton('My TG', url='https://t.me/FATALERROOR')
    z.row(button1, button2)
    bot.send_message(message.chat.id, 'watching this it is important', reply_markup=z)
@bot.message_handler(commands=['memes'])
def memes(message):
    q = types.InlineKeyboardMarkup()
    meeeeeems = types.InlineKeyboardButton('MEMS', url='https://pikabu.ru/tag/%D0%9C%D0%B5%D0%BC%D1%8B')
    q.row(meeeeeems)
    bot.send_message(message.chat.id, 'MORE MEEEEEEMS - Knukcles', reply_markup=q)
@bot.message_handler(content_types=['photo'])
def gug(message):
    s = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton('memes', url='https://klike.net/1048-prikolnye-kartinki-70-foto.html',callback_data='remove')
    s.row(button3)
    bot.send_message(message.chat.id, 'more photos in photos world', reply_markup=s)
def fuf(callback):
    bot.send_message(callback)

@bot.message_handler(content_types=['audio'])
def mug(message):
    bot.reply_to(message, 'Ok, I took this information')

@bot.message_handler(commands=['chta'])
#def chta(message):
    #photo= open(r'C:\Users\Ученик\Downloads\спикер мен (2).jpg','rb')
    #bot.send_message(message.chat.id,photo)

@bot.send_message(content_types = 'text')
def send_books_by_category(message):
    book = MessageController.get_book_by_category(message.text)
    if len(book) == 0:
        bot.send_message(message.chat.id, f'в категории {message.text} нет книг')
    else:
        bot.send_message(message.chat.id,f'Вот какие книги есть у нас в ассортименте: {book}')




if __name__ == '__main__':
    bot.polling(non_stop = True,interval = 0)