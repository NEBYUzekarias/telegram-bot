#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import re
import os
import random
import subprocess
from config import conf
import common

bot = telebot.TeleBot(conf['telegram_token'])

@bot.message_handler(commands=['help', 'start'])
#
# this function will catch the help command
# this command will print a little help to screen
# so users know what commands are availabe
#
def send_welcome(message):
    bot.send_message(message.chat.id, conf['help_msg'])

@bot.message_handler(commands=['thought'])
#
# this will catch the thought command 
# and will return random phrase from mysql
# 
def send_msg(message):
    if message.text.startswith('/thought'):
        kind  = '/thought'
    id = message.text.replace(kind+" ", "")
    print(id)
    output = common._useMysql('getPhrase', id)
    bot.send_message(message.chat.id, output)

# let's bot
bot.polling()
