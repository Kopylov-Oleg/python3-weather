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
        self.ShowWeather = Button(self, text="Узнать погоду", command=self.show_weather)
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
    def __init__(self, master=None, *ap, default_city,**an):
        self.city = StringVar()
        self.city.set(default_city)
        Canvas.__init__(self, master, *ap, **an)

    def draw_weather(self):
        #messagebox.showinfo("Вы ввели", get_weather_data(self.city))
        #self.create_line(0, 0, self.winfo_width(), self.winfo_height(), fill='red', width=1)
        #self.create_line(0, self.winfo_height(), self.winfo_width(), 0, fill='red', width=1)
        #self.create_text(self.winfo_width() / 2, 3 * self.winfo_height() / 4, text = get_real_temp(self.city))
        self.draw_city()
        self.draw_temp()

    def draw_city(self):
        self.create_text(50, 50, text = self.city.get())

    def draw_temp(self):
        temp = str(get_real_temp(self.city.get())) + "°C"
        self.create_text(self.winfo_width() / 2, 3 * self.winfo_height() / 4, text = temp)
        

app = WeatherApp()
app.mainloop()

