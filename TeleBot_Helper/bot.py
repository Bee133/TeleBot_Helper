import telebot
import config
import random
from dateBase import *
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open("./projectPhoto/sticker1.webp", "rb")
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲Бросить кубик")
    item2 = types.KeyboardButton("Добавить дело!")
    item3 = types.KeyboardButton("Посмотреть задачи!")
    item4 = types.KeyboardButton("Удалить задачу!")

    markup.add(item1,item2,item3,item4)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, созданный для записи твоих дел!"
                     .format(message.from_user, bot.get_me()), parse_mode="html", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def speak(message):
    if message.chat.type == "private":
        if message.text == "🎲Бросить кубик":
            k1 = open("./projectPhoto/AnimatedSticker1.tgs", "rb")
            k2 = open("./projectPhoto/AnimatedSticker2.tgs", "rb")
            k3 = open("./projectPhoto/AnimatedSticker3.tgs", "rb")
            k4 = open("./projectPhoto/AnimatedSticker4.tgs", "rb")
            k5 = open("./projectPhoto/AnimatedSticker5.tgs", "rb")
            k6 = open("./projectPhoto/AnimatedSticker6.tgs", "rb")
            grany = random.randint(1,6)
            if grany == 1:
                bot.send_sticker(message.chat.id, k1)
            if grany == 2:
                bot.send_sticker(message.chat.id, k2)
            if grany == 3:
                bot.send_sticker(message.chat.id, k3)
            if grany == 4:
                bot.send_sticker(message.chat.id, k4)
            if grany == 5:
                bot.send_sticker(message.chat.id, k5)
            if grany == 6:
                bot.send_sticker(message.chat.id, k6)
        elif message.text == "Добавить дело!":
            bot.send_message(message.chat.id,"Назови номер задачи как:'Цифра'+'1'\nНазови имя задачи как:'Имя'+'2'\nУкажи описание задачи как:'Описание'+'3'",
                             parse_mode="html")
        elif message.text[-1] == "1":
            bot.send_message(message.chat.id, "Добавляю номер")
            user_id = message.text[:-1]
            cursor.execute(f"INSERT INTO sqlitedb_developers (id) VALUES (?)",(user_id))
            sqlite_connection.commit()
        elif message.text[-1] == "2":
            bot.send_message(message.chat.id, "Добавляю имя")
            user_name = message.text[:-1]
            s = []
            for value in cursor.execute("SELECT * FROM sqlitedb_developers"):
                valueId = str(value[0])
                s.append(int(valueId))
            cursor.execute(f"UPDATE sqlitedb_developers SET name = '{user_name}' WHERE id = '{max(s)}'")
            sqlite_connection.commit()
        elif message.text[-1] == "3":
            bot.send_message(message.chat.id, "Добавляю описание")
            user_inform = message.text[:-1]
            s = []
            for value in cursor.execute("SELECT * FROM sqlitedb_developers"):
                valueId = str(value[0])
                s.append(int(valueId))
            cursor.execute(f"UPDATE sqlitedb_developers SET inform = '{user_inform}' WHERE id = '{max(s)}'")
            sqlite_connection.commit()
        elif message.text == "Посмотреть задачи!":
            for value in cursor.execute("SELECT * FROM sqlitedb_developers"):
                valueId = str(value[0])
                valueName = str(value[1])
                valueInf = str(value[2])
                print(valueId,valueName,valueInf)
                bot.send_message(message.chat.id, valueName+": "+valueInf)
        elif message.text == "Удалить задачу!":
            bot.send_message(message.chat.id, "Выберите номер задачи, которую хотите удалить как:\n'!' + 'Имя' + '!'",
                             parse_mode="html")
        elif message.text[0] == "!" and message.text[-1] == "!":
            userName = message.text[1:-1:]
            cursor.execute(f"DELETE FROM sqlitedb_developers WHERE name = '{userName}'")
            sqlite_connection.commit()
            bot.send_message(message.chat.id,f"Задача, под названием '{userName}', удалена.")
        else:
            bot.send_message(message.chat.id, "Я не знаю, что ответить🥲")



# RUN
bot.polling(none_stop=True)
