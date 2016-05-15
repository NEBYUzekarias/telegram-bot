import telebot
from bs4 import BeautifulSoup
import re
import urllib2
import urllib
import os
import random
import unicodedata
import subprocess

bot = telebot.TeleBot('<YOUR TOKEN HERE>')
path_to_fortune = "/usr/games/fortune"

# Messages
MSG_ON_EMPTY_QUERY = "hey, forgot the query, command is: {} keywords"
NO_RESULTS         = "did't find anything"
GETTING_GIF        = "found it, hang on a sec"
HELP_MSG           = "/photo keywords - find image \n/gif keywords - find gif\n/thought - print a fortune\n/help - show help"

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    ''' this function will catch the help command
	this command will print a little help to screen
	so users know what commands are availabe'''

    bot.send_message(message.chat.id, HELP_MSG)

@bot.message_handler(commands=['photo', 'gif'])
def send_photo(message):
    ''' this function will catch the commands photo and gif,
	will do the search at the sites and return the
	image to chat, to do so the function will download the
	image locally first to send it after.'''

    tipo = {
        '/photo': ['bing.net', 'image.jpg', 'http://www.bing.com/images/search?q={}&qs=n&form=QBLH&scope=images&sc=9-3&sp=-1'],
        '/gif'  : ['giphy.com', 'image.gif', 'http://giphy.com/search/{}']
    }

    if message.text.startswith('/photo'):
        kind  = '/photo'
    elif message.text.startswith('/gif'):
        kind  = '/gif'

    image_type = "Action"
    query = message.text.replace(kind+" ", "")
    # remove accents from query
    query = remove_accents(query)
    if query != kind:
        # set the query and assign it to the url
        query = query.split()
        query ='+'.join(query)
        url = tipo[kind][2].format(query)
        # header and request
        header = {'User-Agent': 'Mozilla/5.0'} 
        soup = get_soup(url,header)
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
                bot.send_message(message.chat.id, GETTING_GIF)
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
            bot.send_message(message.chat.id, NO_RESULTS)
    else:
        bot.send_message(message.chat.id, MSG_ON_EMPTY_QUERY.format(kind))

@bot.message_handler(commands=['thought'])
def send_photo(message):
    ''' this will catch the thought command 
	and will run the command fortune returning
	the output to chat '''

    output = subprocess.Popen([path_to_fortune], stdout=subprocess.PIPE).communicate()[0]
    bot.send_message(message.chat.id, output)

def get_soup(url,header):
    ''' open url and make the request '''
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)))

def remove_accents(input_str):
    ''' remove accents from input'''
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

# let's bot
bot.polling()
