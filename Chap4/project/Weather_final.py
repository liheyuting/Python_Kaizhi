#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/9 下午1:20
# @Author  : Dora
# @File    : hello.py

from flask import Flask, render_template, request
from weather import fetchWeather
from database  import insert_data, retrieve_data, get_history,update

#地点: hangzhou, 天气: 多云, 温度: 26, 更新时间


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_request', methods=['POST', 'GET'])
def home():
        city = request.args.get("city")
        if request.args.get('btn') == "查询":
            try:
                result = retrieve_data(city)
                return render_template('weather.html',result=result)
            except TypeError:
                try:
                    location, weather, temper, day = fetchWeather(city)
                    insert_data(location, weather, temper, day)
                    result = '''
地点: {},
天气: {},
温度: {},
更新时间: {}/n'''.format(location, weather ,temper, day)
                    return render_template('weather.html', result=result)

                except KeyError:
                    result = "Invalid command. Type 'help' to check the available commands."
                    return render_template('404.html', result=result)

        elif request.args.get('btn') == "帮助":
            return render_template('help.html')

        elif request.args.get('btn') == "历史":
            history = get_history()
            return render_template('history.html', result = history)

        elif request.args.get('btn') == "更新":
            try:
                location, weather=city.split(' ')
                weather_list = ["晴", "小雨", "大雨", "阴天", "大雪", "中雪", "小雪"]
                if weather in weather_list:
                    update(location, weather)
                    return render_template('update.html')
                else:
                    result = "请正确输入信息，例如：[北京 多云]"
                    return render_template('404.html', result=result)
            except ValueError:
                result = "Invalid command. Type 'help' to check the available commands."
                return render_template('404.html', result=result)


        else:
            result = "Invalid command. Type 'help' to check the available commands."
            return render_template('404.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)