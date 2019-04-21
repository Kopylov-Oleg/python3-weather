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

from tkinter import *
from tkinter import messagebox

class WeatherApp(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.title("Weather Application")
        self.grid(sticky=N+E+S+W)
        self.new_city = StringVar()
        self.create()
        self.adjust()

    def create(self):
        self.Canvas = Paint(self, default_city="moscow")
        self.Canvas.grid(row=0, column=0, rowspan=9, columnspan=5, sticky=N+E+S+W)
        self.CityEntry = Entry(self, textvariable=self.new_city)
        self.CityEntry.grid(row=10, column=1, sticky=N+E+S+W)
        self.ShowWeather = Button(self, text="Show weather", command=self.show_weather)
        self.ShowWeather.grid(row=10, column=3, sticky=N+E+S+W)

    def adjust(self):
        for i in range(5):
            self.columnconfigure(i, weight=1, minsize = 30)
        for i in range(12):
            self.rowconfigure(i, weight=1, minsize = 30)

    def show_weather(self):
        messagebox.showinfo("Вы ввели", get_weather_data(self.new_city.get()))
        self.Canvas.city.set(self.new_city.get())

class Paint(Canvas):
    def __init__(self, master=None, *ap, default_city, **an):
        self.city = StringVar()
        self.city.set(default_city)
        Canvas.__init__(self, master, *ap, **an)

app = WeatherApp()
app.mainloop()
