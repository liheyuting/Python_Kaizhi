# Ch2

# import requests
输入requests模块

```
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
```
从API中获得相对应的数据

```
    try:
        fetchWeather(location)
        demo = fetchWeather(location)
        print(demo)
        history.append(demo)
    except KeyError:
```

在运行时判断
