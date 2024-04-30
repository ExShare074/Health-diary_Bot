# бот Джарвис, который напомнит вам обо всем, о чем вы могли забыть

import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot("6783028161:AAHqm9saOwaTQwBmJbtypOsle5oiYrK_SAU")  # Вставляем свой токен

gif_url = "https://i.pinimg.com/originals/1d/15/45/1d15457b2054d0d1c1cebd37eae3026e.gif"
gif_url_2 = "https://i.pinimg.com/originals/a2/64/b9/a264b94873b534f7affe1dc03c1497fc.gif"
gif_url_3 = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZThzdmsxeW5mZjd1aHZhNWZqbjFvYnR4OHpuOHM3ZWxjcHdtaHY3NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FHlMJHSx5sGBi/giphy.gif"
gif_url_4 = "https://media.giphy.com/media/Ax2GE5TKYSUzvzfGEH/giphy.gif?cid=790b7611539f1f8vs8ovsxp5on9qcjwzmt66qor7m7i6ai1v&ep=v1_gifs_search&rid=giphy.gif&ct=g"
gif_url_5 = "https://media.giphy.com/media/PrTCHhXyn6ZtNF5nly/giphy.gif?cid=790b7611842m0e58hlsjgm53duuq0qofv58yd29arpsusq44&ep=v1_gifs_search&rid=giphy.gif&ct=g"


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, text="Привет! Я бот Джарвис, который будет тебе напоминать\
    сделать разминку, принять витамины и следить за твоим рационом!")
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()


@bot.message_handler(commands=["fact"])
def fact_message(message):
    list_of_facts = [
        "Ежедневная разминка улучшает кровообращение в организме, что помогает предотвратить спазмы мышц\n\n",
        "Регулярное выполнение утренней разминки помогает пробудить организм и подготовить его к активному дню\n\n",
        "Растяжка улучшает гибкость мышц и суставов, что снижает риск получения травм и болей в спине и суставах\n\n",
        "Занятие растяжкой или разминкой улучшает психологическое состояние, снижает уровень стресса и усталости\n\n",
        "Регулярная разминка помогает улучшить осанку и предотвратить проблемы со спиной и суставами, связанными с сидячим образом жизни"]
    random_fact = random.choice(list_of_facts)
    bot.reply_to(message, text=f"Лови факт о разминке: {random_fact}")


def send_reminders(chat_id):
    first_reminder = "18:37"
    second_reminder = "08:00"
    three_reminder = "13:00"
    end_reminder = "17:52"
    water1_reminder = "18:37"
    vitamin1_reminder = "18:37"
    creatin_reminder = "18:38"
    vitamin2_reminder = "13:00"
    vitamin3_reminder = "18:57"
    vitamin4_reminder = "18:38"

    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_reminder:
            bot.send_message(chat_id, "Разомни мышцу чемпион!")
            bot.send_document(chat_id, gif_url)  # Отправляем gif-картинку
            time.sleep(61)  # Проверяем время каждую минуту

        if now == second_reminder:
            bot.send_message(chat_id, "Разомни мышцу чемпион!")
            bot.send_document(chat_id, gif_url)  # Отправляем gif-картинку
            time.sleep(61)  # Проверяем время каждую минуту

        if now == three_reminder:
            bot.send_message(chat_id, "Разомни мышцу чемпион!")
            bot.send_document(chat_id, gif_url)  # Отправляем gif-картинку
            time.sleep(61)  # Проверяем время каждую минуту

        if now == end_reminder:
            bot.send_message(chat_id, "Разомни мышцу чемпион!")
            bot.send_document(chat_id, gif_url)  # Отправляем gif-картинку
            time.sleep(61)  # Проверяем время каждую минуту

        if now == water1_reminder:
            bot.send_message(chat_id, "Выпей на тощак стакан воды!")
            bot.send_document(chat_id, gif_url_2)  # Отправляем gif-картинку
            time.sleep(61)  # Проверяем время каждую минуту

        if now == vitamin1_reminder:
            bot.send_message(chat_id, "Выпей месте с едой таблетку Omega-3 и DMAE!")
            bot.send_document(chat_id, gif_url_3)  # Отправляем gif-картинку
            time.sleep(61)  # Проверяем время каждую минуту

        if now == creatin_reminder:
            bot.send_message(chat_id,
                             "Прими 5гр Креатина (Факт о креатине - это самая безопасная в мире спортивная добавка, "
                             "наполняет мышцы водой, укрепляет кости и связки, буст +20 к твоей силе!")
            bot.send_document(chat_id, gif_url_4)  # Отправляем gif-картинку
            time.sleep(61)  # Проверяем время каждую минуту

        if now == vitamin2_reminder:
            bot.send_message(chat_id, "Выпей месте с едой таблетку Omega-3!")
            bot.send_document(chat_id, gif_url)  # Отправляем gif-картинку
            time.sleep(61)  # Проверяем время каждую минуту

        if now == vitamin3_reminder:
            bot.send_message(chat_id, "Выпей месте с едой таблетку Omega-3 и DMAE!!")
            bot.send_document(chat_id, gif_url_3)  # Отправляем gif-картинку
            time.sleep(61)  # Проверяем время каждую минуту

        if now == vitamin4_reminder:
            bot.send_message(chat_id, "Выпей таблетку Мелатонина (Факт о Мелатонине - "
                                      "Прием мелатонина вечером помогает улучшить качество сна и "
                                      "синхронизировать циркадианный ритм организма.!!")
            bot.send_document(chat_id, gif_url_5)  # Отправляем gif-картинку
            time.sleep(61)  # Проверяем время каждую минуту

        time.sleep(1)


bot.polling(none_stop=True)  # Запускаем бота с опцией none_stop=True, чтобы бот не выключался

