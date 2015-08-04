# coding=utf-8
__author__ = '胖'

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id = \'9527\' ')
print(cursor.fetchall())
cursor.close()
conn.close()

