import requests

# https://www.apixu.com/api-explorer.aspx?key=3fad82dbce9a43a8bed183010191904

def get_weather_data(name):
    url = f"http://api.apixu.com/v1/current.json?key=3fad82dbce9a43a8bed183010191904&q={name}"
    r = requests.get(url)
    return r.json()


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

