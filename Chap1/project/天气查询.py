#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 下午9:51
# @Author  : Dora
# @File    : 天气查询.py


input_word = input("请输入指令或您要查询的城市名")

def city_name(city, weather):
    city_history=[]
    weather_history=[]
    if city in city_list:
        weather = city_list[city]
        print(city, weather)
    else:
        print("请输入指令或您要查询的城市名")
    city_history.append(city)
    weather_history.append(weather)

def help_help():
    print(
        """
        请输入城市名，查询该城市的天气；
        输入help，获取帮助文档；
        输入history，获取查询历史
        输入quit，退出天气查询系统
        """
          )

def quit_quit():
    exit(0)

def history():
    for city, weather in range(city_history, weather_history):
        print(city, weather)
    exit(0)

with open('weather_info.txt','r') as city_list:
    city_list.read()

for line in city_list.readlines():
    

