from tkinter import *
from tkinter import messagebox
from weather_logic import *

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
        self.Canvas.city.set(self.new_city.get())
        self.Canvas.draw_weather()

class Paint(Canvas):
    def __init__(self, master=None, *ap, default_city, **an):
        self.city = StringVar()
        self.city.set(default_city)
        Canvas.__init__(self, master, *ap, **an)

    def draw_weather(self):
        messagebox.showinfo("Вы ввели", get_weather_data(self.city))

app = WeatherApp()
app.mainloop()

