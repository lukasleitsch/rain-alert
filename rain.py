#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import telegram
import config

bot = telegram.Bot(token=config.token)

# use P1 header pin numbering convention
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN)

input = GPIO.input(11)

bot.send_message(chat_id=config.chat_id, text="💤  Warte auf den Regen...")

try:
    while True:
        GPIO.wait_for_edge(11, GPIO.FALLING)
        bot.send_message(chat_id=config.chat_id, text="🌧  Es regnet!")

except KeyboardInterrupt:
    GPIO.cleanup()
    print ('Bye')
