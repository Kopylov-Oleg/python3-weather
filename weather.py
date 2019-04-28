from tkinter import *
from tkinter import messagebox
from weather_logic import *
from canvas import gui

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
        self.Canvas = Paint(self, default_city="")
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
        self.Canvas.weather_data = get_weather_data(self.new_city.get())
        self.Canvas.draw_weather()

class Paint(Canvas):
    def __init__(self, master=None, *ap, default_city,**an):
        self.city = StringVar()
        self.city.set(default_city)
        self.weather_data = ""
        Canvas.__init__(self, master, *ap, **an)
        self.bind('<Configure>', self.configure)
    
    def configure(self, event):
        if (self.city.get() != ""):
            messagebox.showinfo("Размер окна:", str(str(event.width) + " x " + str(event.height)))
            #self.draw_weather()

    def draw_weather(self):
        self.delete("all")
        #messagebox.showinfo("Вы ввели", get_weather_data(self.city.get()))
        gui(self, self.weather_data)

    def draw_city(self):
        self.create_text(self.winfo_width() / 4, self.winfo_height() / 5, text = self.city.get())

    def draw_time(self):
        time = "00:00"
        self.create_text(3 * self.winfo_width() / 4, self.winfo_height() / 5, text = time)

    def draw_conditions(self):
        conditions = str(get_conditions(self.city.get()))
        self.create_text(self.winfo_width() / 4, 4 * self.winfo_height() / 5, text = conditions)

    def draw_temp(self):
        temp = str(get_real_temp(self.city.get())) + "°C"
        self.create_text(3 * self.winfo_width() / 4, 4 * self.winfo_height() / 5, text = temp)

    def draw_weather_picture(self):
        conditions = str(get_conditions(self.city.get()))
        if (conditions == "Sunny"):
            self.draw_sunny()
        elif (conditions == "Partly cloudy"):
            self.draw_partly_cloudly()
        elif (conditions == "Mist"):
            self.draw_mist()
        elif (conditions == "Light rain"):
            self.draw_light_rain()
        elif (conditions == "Overcast"):
            self.draw_overcast()
        elif (conditions == "Clear"):
            self.draw_clear()
        elif (conditions == "Patchy light rain with thunder"):
            self.draw_patchy_light_rain_with_thunder()
        elif (conditions == "Moderate or heavy rain with thunder"):
            self.draw_moderate_or_heavy_rain_with_thunder()

    def draw_sunny(self):
        color = 'yellow'
        self.create_oval(self.winfo_width()/4, self.winfo_height()/4, 3*self.winfo_width()/4, 3*self.winfo_height()/4, fill=color, width=3)

    def draw_partly_cloudly(self):
        color = 'grey'
        self.create_oval(self.winfo_width()/4, self.winfo_height()/4, 3*self.winfo_width()/4, 3*self.winfo_height()/4, fill=color, width=3)

    def draw_mist(self):
        color = 'white'
        self.create_oval(self.winfo_width()/4, self.winfo_height()/4, 3*self.winfo_width()/4, 3*self.winfo_height()/4, fill=color, width=3)

    def draw_light_rain(self):
        color = 'light blue'
        self.create_oval(self.winfo_width()/4, self.winfo_height()/4, 3*self.winfo_width()/4, 3*self.winfo_height()/4, fill=color, width=3)

    def draw_overcast(self):
        color = 'bisque2'
        self.create_oval(self.winfo_width()/4, self.winfo_height()/4, 3*self.winfo_width()/4, 3*self.winfo_height()/4, fill=color, width=3)

    def draw_clear(self):
        color = 'lightcyan2'
        self.create_oval(self.winfo_width()/4, self.winfo_height()/4, 3*self.winfo_width()/4, 3*self.winfo_height()/4, fill=color, width=3)

    def draw_patchy_light_rain_with_thunder(self):
        color = 'gold3'
        self.create_oval(self.winfo_width()/4, self.winfo_height()/4, 3*self.winfo_width()/4, 3*self.winfo_height()/4, fill=color, width=3)

    def draw_moderate_or_heavy_rain_with_thunder(self):
        color = 'gold4'
        self.create_oval(self.winfo_width()/4, self.winfo_height()/4, 3*self.winfo_width()/4, 3*self.winfo_height()/4, fill=color, width=3)

app = WeatherApp()
app.mainloop()
