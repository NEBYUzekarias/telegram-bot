#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
import re
import urllib2
import urllib
import os
import random
import subprocess
from config import conf
import common

bot = telebot.TeleBot(conf['telegram_token'])

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    ''' this function will catch the help command
	this command will print a little help to screen
	so users know what commands are availabe'''
    bot.send_message(message.chat.id, conf['help_msg'])

@bot.message_handler(commands=['photo', 'gif'])
def send_photo(message):
    ''' this function will catch the commands photo and gif,
	will do the search at the sites and return the
	image to chat, to do so the function will download the
	image locally first to send it after.'''
    # params for photo and gif
    tipo = {
        '/photo': ['bing.net', 'image.jpg', 'http://www.bing.com/images/search?q={}&qs=n&form=QBLH&scope=images&sc=9-3&sp=-1'],
        '/gif'  : ['giphy.com', 'image.gif', 'http://giphy.com/search/{}']
    }
    # set kind dependind of tipo
    if message.text.startswith('/photo'):
        kind  = '/photo'
    elif message.text.startswith('/gif'):
        kind  = '/gif'
    # get query
    query = message.text.replace(kind+" ", "")
    # when no keywords came the replace does not
    # match coz there is no space after kind 
    # and query is eq to kind
    if query != kind:
        # remove accents from query
        query = common._removeAccents(query)
        # set the query and assign it to the url
        query = query.split()
        query = '+'.join(query)
        url = tipo[kind][2].format(query)
        # header and request
        header = {'User-Agent': 'Mozilla/5.0'} 
        soup = common._getSoup(url,header)
        images = [a['src'] for a in soup.find_all("img", {"src": re.compile(tipo[kind][0])})]
        # if result
        if images:
            # read a random result
            img = random.choice(images)
            if kind == '/gif':
                # giphy return the urls with a _s 
                # wich is the first frame of the gif
                # to get the gif remove it.
                img = img.replace('200_s', '200')
                path_to_img = os.path.join("pics/", tipo[kind][1])
                bot.send_message(message.chat.id, conf['getting_gif'])
                urllib.urlretrieve(img, path_to_img) 
                # send gif to telegram
                # NOTE: gif must be send as document
                photo = open(path_to_img, 'rb')
                bot.send_document(message.chat.id, photo)
            else:
                raw_img = urllib2.urlopen(img).read()
                # get the image
                path_to_img = os.path.join("pics/", tipo[kind][1])
                f = open(path_to_img, 'wb')
                f.write(raw_img)
                f.close()
                # send image to telegram
                photo = open(path_to_img, 'rb')
                bot.send_photo(message.chat.id, photo)
        else:
            bot.send_message(message.chat.id, conf['no_results'])
    else:
        bot.send_message(message.chat.id, conf['msg_on_empty_query'].format(kind))

@bot.message_handler(commands=['thought'])
def send_msg(message):
    ''' this will catch the thought command 
	and will return random phrase from mysql'''
    output = common._useMysql('getPhrase')
    bot.send_message(message.chat.id, output)

# let's bot
bot.polling()
