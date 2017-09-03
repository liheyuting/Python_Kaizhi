#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/30 下午9:37
# @Author  : Dora
# @File    : Weather_test_bushu.py

from flask import Flask, request, render_template
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
    weather_time = weather_result['results'][0]['last_update']
    return """
地点: %s,
天气: %s,
温度: %s,
更新时间: %s
""" % (location, weather_dict['text'], weather_dict['temperature'], weather_time)
history = []

app = Flask(__name__)
@app.route("/", methods=['POST','GET'] )

def weather():
    btn = ""
    btn0 = ""
    print(request.form)

    if request.form['btn'] == "查询":
            demo = fetchWeather(btn0)
            btn = demo
            history.append(demo)

    elif request.form['btn'] == "帮助":
            btn = """
                请输入城市名，查询该城市的天气；
                输入help，获取帮助文档；
                输入history，获取查询历史
                输入quit，退出天气查询系统"""

    elif request.form['btn'] == "历史":
        for n in range(0, len(history)):
                btn = history[n]
        else:
                btn = "Invalid command. Type 'help' to check the available commands."
        return render_template('html/weather.html', btn = btn)

app.run()