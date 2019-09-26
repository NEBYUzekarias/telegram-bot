#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector
from config import conf
from bs4 import BeautifulSoup
import urllib.request as urllib2
import unicodedata
#
# Function that will do the mysql stuff
# 
# @param whatToDo 
# @return mixed
#
def _useMysql(whatToDo,id,  param=False):
    querys  = { 
            # This example works fine and is fast if you only when let's say 5000 rows. 
            # As soon as you have 10000 rows the overhead for sorting the rows becomes important.
            # 'getPhrase' :   "SELECT phrase FROM phraseList ORDER BY RAND() LIMIT 1",
            'getPhrase' :   "SELECT phrase FROM phraseList WHERE id = ",
            'insertPhrase': "INSERT INTO phraseList (phrase) VALUE(%s)",
    }
    # connects to db
    dsn     = mysql.connector.connect(**conf['mysql'])
    try:
        cursor  = dsn.cursor()
        if whatToDo == 'insertPhrase':
            cursor.execute(querys[whatToDo], (param,))
            dsn.commit()
            return True
        else:
            cursor.execute(querys[whatToDo]+ id )
            result  = cursor.fetchone()
            return result
    finally:
        cursor.close()
        dsn.close()
#
# Function that will open/request an url
#
# @param url        url to open
# @param header     headers pass on request
#
def _getSoup(url,header):
    some = urllib2.Request(url,headers=header)
    some = urllib2.urlopen(some)
    return BeautifulSoup(some)
#
# Function that will remove 
# accents from string
#
# @param input_str  string from where the function have to remove accents
#
def _removeAccents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii
