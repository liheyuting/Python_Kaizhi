#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/12 下午8:29
# @Author  : Dora
# @File    : databace.py

import sqlite3
import time

def create_db():
    con = sqlite3.connect('weather.db')
    with con:
        cur = con.cursor()
        cur.execute('DROP table if exists Weathers')
        cur.execute('CREATE table Weathers(location text, weather text, temper text, day text)')
        print("数据库已更新")


def insert_data(location, weather ,temper, day):
    con = sqlite3.connect('weather.db')
    with con:
        cur = con.cursor()
        cur.execute('INSERT into Weathers values(?,?,?,?)',(location, weather ,temper, day))

def retrieve_data(location):
    con = sqlite3.connect('weather.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT location, weather ,temper, day FROM Weathers where location =:location',{"location":location })
        row = cur.fetchone()
        weather_str = '{},{},{},{}'.format(row[0],row[1],row[2],row[3])
        return weather_str

def get_history():
    con=sqlite3.connect('weather.db')
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM weathers')
        row = cur.fetchall()
    return row


def update(location,weather):
    con = sqlite3.connect('weather.db')
    with con:
        cur = con.cursor()
        cur.execute("UPDATE Weathers set weather= ? where location = ?", (weather,location))

if __name__ == '__main__':
    while True:
        create_db()
        time.sleep(10800)
    #insert_data('9月4日', '上海', '多云', '30')
    #update("北京","小雨")
    #print(get_history())
