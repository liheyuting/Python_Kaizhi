#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/9 下午1:20
# @Author  : Dora
# @File    : hello.py

from flask import Flask, render_template, request
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

app = Flask(__name__)
history=[]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_request', methods=['POST', 'GET'])
def home():
    try:
        city = request.args.get("city")
        result = fetchWeather(city)
        history.append(result)
        return render_template('weather.html', result=result)
    except KeyError:
        if request.args.get('btn') == "帮助":
            return render_template('help.html')
        elif request.args.get('btn') == "历史":
            return render_template('history.html', result= history)
        else:
            result = "Invalid command. Type 'help' to check the available commands."
            return render_template('404.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)