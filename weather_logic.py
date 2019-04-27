import requests
import functools

# Weather server & API:
# https://www.apixu.com/api-explorer.aspx?key=3fad82dbce9a43a8bed183010191904

@functools.lru_cache()
def get_weather_data(name):
    print("Server query")
    url = f"http://api.apixu.com/v1/current.json?key=3fad82dbce9a43a8bed183010191904&q={name}"
    r = requests.get(url)
    answer = r.json()
    if 'error' not in answer:
        return answer
    else:
        raise Exception(answer['error']['message'])



def console_print_weather(city):
    d = get_weather_data(city)
    real_temp = d['current']['temp_c']
    feels_like = d['current']['feelslike_c']
    conditions = d['current']['condition']['text']
    day_night = ['ночь', 'день'][d['current']['is_day']]
    wind_speed = d['current']['wind_kph']
    visibility = d['current']['vis_km']
    
    text = f"Погода в {city}:\nТемпература воздуха: {real_temp}˚C\nОщущается как: {feels_like}\n" + \
           f"Погодные условия: {conditions}\nВремя суток: {day_night}\nВетер: {wind_speed} км/ч\nВидимость: {visibility}км\n"
        
    print(text)
    

""" An idea of implementation change - Just in case.
class CityData:
    REFRESH_TIME = 15
    
    def __init__(self):
        self.cities = {}
        self.city_added = {}
    
    def __getitem__(self, city_name):
        if city_name in self.cities:
            if time.hour == self.city_added[city_name][0] and time.minute - self.city_added[city_name][1] <= self.REFRESH_TIME:
                return self.cities[city_name]
            else:
                self.cities[city_name] = get_weather_data(city_name)
                self.city_added[city_name] = [datetime.date(), datetime.time()]
"""
    
# запрос к серверу при каждом вызове функций вида get_*(city_name) - неправильное проектное решение.
# изменено.
# Функции, зависящие от этого ДАЖЕ НЕ придется переделывать...
# (не нужно забывать что у нас ограниченное число обращений к серверу в месяц)
# решено с использованием lru_cache. Работает нормально, тк не подразумевается что пользователь будет держать приложение часами в online. Если это так - убираем lru_cache и просто используем больше обращений к серверу. 
# Пока что в любом случае с помощью кэша тратим меньше обращений к серверу.

# !!!> также не нужно забывать что get_weather_data кидает Exception если не находит нужный город  
# Proposal: отлавливать исключения в функции, вызывающей get_...().
    
def get_time(city):
    d = get_weather_data(city)
    return d['location']['localtime'].split()[1]
    
def get_real_temp(city):
    d = get_weather_data(city)
    return d['current']['temp_c']

def get_feels_like(city):
    d = get_weather_data(city)
    return d['current']['feelslike_c']

def get_conditions(city):
    d = get_weather_data(city)
    return d['current']['condition']['text']

def get_day_night(city):
    d = get_weather_data(city)
    return ['ночь', 'день'][d['current']['is_day']]

def get_wind_speed(city):
    d = get_weather_data(city)
    return d['current']['wind_kph']

def get_visibility(city):
    d = get_weather_data(city)
    return d['current']['vis_km']

