import telebot
import sqlite3
import buttons
import database
from googletrans import Translator
from telebot.types import ReplyKeyboardRemove
from database import register_user, check_user, add_user_words
from buttons import contact_button, translate_button, language_button

trns = Translator()



db = sqlite3.connect('dat.db')
sql = db.cursor()

# from .database import add_contact

TOKEN = '6618391908:AAGdqdaDpxdBbLNnWAnveiS9NFPE3RSbmSw'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    USERS = database.check_user(message.from_user.id)
    print(USERS)
    if USERS:
        bot.send_message(message.from_user.id,'TO start translate, user')

    else:
        bot.send_message(message.from_user.id, 'To start the bot, share your contact', reply_markup=buttons.contact_button())
        bot.register_next_step_handler(message, get_contact)




def get_contact(message):
    if message.contact:
        PhoneNumber = message.contact.phone_number
        FirstName = message.contact.first_name
        Telegram_ID = message.from_user.id

        database.register_user(Telegram_ID, FirstName, PhoneNumber)


        bot.send_message(message.from_user.id, 'To start translete, user the button', reply_markup=buttons.translate_button())
        # bot.send_message(message.from_user.id, 'Which languge do you choose?', reply_markup=buttons.language_button())
    else:
        bot.send_message(message.from_user.id, 'Please to share your cantact use the button', reply_markup=buttons.contact_button())
        bot.register_next_step_handler(message, get_contact)

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text == 'Translate':
        bot.send_message(message.from_user.id, 'Choice which langues you want to translate', reply_markup=buttons.language_button())
        bot.register_next_step_handler(message, get_language)


def get_language(message):
    to_language = message.text

    bot.send_message(message.from_user.id, 'Send text to translate', reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, translate_text, to_language)


def translate_text(message, to_language):
    text = message.text

    result = trns.translate(text=text, dest=to_language).text

    bot.send_message(message.from_user.id, result, reply_markup=buttons.translate_button())

bot.polling()