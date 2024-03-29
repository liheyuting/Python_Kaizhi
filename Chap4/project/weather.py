#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/21 下午10:34
# @Author  : Dora
# @File    : weather.py

import requests

KEY = '5cjf78nhu2nhavih'
LANGUAGE = 'zh-Hans'
UNIT = 'C'

def fetchWeather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=100)
    weather_result = result.json()
    weather_dict = weather_result['results'][0]['now']
    day = weather_result['results'][0]['last_update']
    weather = weather_dict['text']
    temper = weather_dict['temperature']
    #return """
#地点: %s,
#天气: %s,
#温度: %s,
#更新时间: %s
#""" % (location, weather_dict['text'], weather_dict['temperature'], weather_time)
    return location, weather ,temper, day

#地点: hangzhou, 天气: 多云, 温度: 26, 更新时间




