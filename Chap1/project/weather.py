#!/usr/bin/env python3
# -*- coding: utf-8 -*-

city_weather = {}
history = []

with open('weather_info.txt') as list1:
    for info in list1.readlines():
        n = info.split(",")
        city_weather[n[0]] = n[1]

while True:
    Q=input("请输入指令或是您想要查询的城市：")
    if Q == "help":
        print("""
            请输入城市名，查询该城市的天气；
            输入help，获取帮助文档；
            输入history，获取查询历史
            输入quit，退出天气查询系统
            """)
    elif Q in city_weather:
            print(Q, city_weather[Q])
            history.append(Q + ": " + city_weather[Q])

    elif Q == "quit":
        print("退出")
        exit(0)

    elif Q == "history":
        print(history)

    else:
        print("请输入正确指令或是城市")



