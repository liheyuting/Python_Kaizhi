#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 下午10:34
# @Author  : Dora
# @File    : test.py

import requests

KEY = '5cjf78nhu2nhavih'
LANGUAGE = 'zh-Hans'
UNIT = 'C'

def fetchWeather(location):
    try:
        result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=1)
        weather_result = result.json()
        weather_dict = weather_result['results'][0]['now']
        weather_time = weather_result['results'][0]['last_update']
        return """
地点: %s,
天气: %s,
温度: %s,
更新时间: %s
""" % (location, weather_dict['text'], weather_dict['temperature'], weather_time)
    except:
        print("Invalid command. Type 'help' to check the available commands.")

history = []

while True:
    location = input("请输入你想查询的地方：")
    demo=fetchWeather(location)
    if location == "help":
        print("""
请输入城市名，查询该城市的天气；
输入help，获取帮助文档；
输入history，获取查询历史
输入quit，退出天气查询系统""")

    elif location == "quit":
        print("退出")
        exit(0)

    elif location == "history":
        for n in range(0,len(history)):
            print(history[n])
    else:
        print(demo)
        history.append(demo)


