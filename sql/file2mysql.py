#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')
import common

# CHANGE HERE THE NAME OF FILE THAT
# this is the part that we replace with our data 
file_to_import = '/home/neba/Documents/projects/telegram/telegram-bot/sql/phrases/art'

#
# Import the phrases that you want to
# add to the /thought command
#
# This script will parse the file
# and will add the prases to the phraseList
# in the mysql, you can import more then once
# or extend the bot to have more than one /command
# that replies from the db
#
with open(file_to_import) as f:
    phrase = ''
    for line in f:
        if '%' in line:
            common._useMysql('insertPhrase', phrase)
            phrase = ''
        else:
            phrase = phrase+line
