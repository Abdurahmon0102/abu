import sqlite3
from datetime import datetime

db = sqlite3.connect('dat.db')
sql = db.cursor()

db.execute(f"CREATE TABLE IF NOT EXISTS USERS (ID INTEGER PRIMAY KEY AUTOINCEREMENT, FirstName TEXT, Telegram_ID INTEGER, PhoneNumber TEXT, Reg_date DATETIMI)")
db.execute(f"CREATE TABLE IF NOT EXISTS USER_WORDS (ID INTEGER PRIMAY KEY AUTOINCEREMENT, Telegram_ID INTEGER, Text TEXT, Translete TEXT, Added_date DATETIMI)")


def register_user(Telegram_ID, FirstName, PhoneNumber):
    db = sqlite3.connect('dat.db')
    sql = db.cursor()

    sql.execute("INSERT INTO USERS (Telegram_ID, FirstName, PhoneNumber, Reg_date) VALUES (?,?,?,?);", (Telegram_ID, FirstName, PhoneNumber, datetime.now()))

    db.commit()
    db.close()


def check_user(Telegram_ID):
    db = sqlite3.connect('dat.db')
    sql = db.cursor()

    user = sql.execute("SELECT Telegram_ID FROM users WHERE Telegram_ID=?;", (Telegram_ID,)).fetchone()

    if user:
        return True
    
    else:
        return False

def add_user_words(Telegram_ID, Text, Translete):
    db = sqlite3.connect('dat.db')
    sql.execute("INSERT INTO USER_WORDS (Telegram_ID, Text, Translete, Added_date) VALUES (?,?,?,?);", (Telegram_ID, Text, Translete, datetime.now()))

    db.commit()
    db.close()