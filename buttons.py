from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def contact_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Share contact', request_contact=True)
    kb.add(button)

    
    return kb


def translate_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    button = KeyboardButton('Translate')
    kb.add(button)
    
    return kb


def language_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    ru = KeyboardButton('RU')
    uz = KeyboardButton('UZ')
    en = KeyboardButton('EN')
    es = KeyboardButton('ES')

    kb.add(ru, uz, en, es)

    return kb

    