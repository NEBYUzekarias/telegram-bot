#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector
from config import conf
#
# Method that will do the mysql stuff
# 
# @param whatToDo 
# @return string
#
def _useMysql(whatToDo, param=False):
    querys  = { 
            # This example works fine and is fast if you only when let's say 5000 rows. 
            # As soon as you have 10000 rows the overhead for sorting the rows becomes important.
            'getPhrase' :   "SELECT phrase FROM phraseList ORDER BY RAND() LIMIT 1",
            'insertPhrase': "INSERT INTO phraseList (phrase) VALUE(%s)",
    }
    # connects to db
    dsn     = mysql.connector.connect(**conf['mysql'])
    try:
        cursor  = dsn.cursor()
        if whatToDo == 'getPhrase':
            cursor.execute(querys[whatToDo])
            result  = cursor.fetchone()
            return result
        else:
            cursor.execute(querys[whatToDo], (param,))
            dsn.commit()
            return True
    finally:
        cursor.close()
        dsn.close()
