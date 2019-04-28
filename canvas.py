from tkinter import *
from tkinter import ttk
import random
import math

from weather_logic import get_weather_data

if __name__ == '__main__':
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

class Color():
    def __init__(self, rgb):
        self.rgb = list(rgb)
        #self.rgb = [min(255, c) for c in [max(0, c) for c in self.rgb]]

    @classmethod
    def random(cls):
        return cls(random.randint(0, 255) for _ in range(3))


    def __iter__(self):
        return iter(self.rgb)

    def clamp(self):
        return Color(min(255, c) for c in [max(0, c) for c in self.rgb])

    def __add__(self, other):
        if type(other) in (int, float):
            return Color(list(map(lambda x : int(x + other), self.rgb)))
        else:
            r1, g1, b1 = self.rgb
            r2, g2, b2 = other.rgb
            return Color([int(r1+r2), int(g1+g2), int(b1+b2)])

    def __sub__(self, other):
        if type(other) in (int, float):
            return Color(list(map(lambda x : int(x - other), self.rgb)))
        else:
            r1, g1, b1 = self.rgb
            r2, g2, b2 = other.rgb
            return Color([int(r1-r2), int(g1-g2), int(b1-b2)])

    def __mul__(self, k):
        return Color(map(lambda x : int(x * k), self.rgb))

    def __floordiv__(self, k):
        return Color(map(lambda x : int(x // k), self.rgb))

    def __truediv__(self, k):
        return Color(map(lambda x : x / k, self.rgb))

    def to_hex(self):
        return '#' + ''.join('{:02X}'.format(a) for a in self.rgb)

    def __str__(self):
        return '(' + ', '.join(list(map(str, self.rgb))) + ')'


def rgb_to_hex(rgb):
    return rgb.to_hex()


def draw_grad(canvas, start_color, end_color, H=800, W=1280, step_size=20):
    start_color = Color(start_color)
    end_color = Color(end_color)
    value = start_color
    steps = H / step_size
    inc = (start_color - end_color) / steps

    for y in range(0, H, step_size):
        for x in range(0, W, step_size):
            #print(value)
            #canvas.create_rectangle(i, j, i+step_size, j+step_size, outline='', fill=rgb_to_hex(value))
            canvas.create_line(x, y, x + W, y, fill=rgb_to_hex(value.clamp()),width=step_size)

        value += inc
        value = Color(math.floor(v) for v in value.rgb).clamp()


def draw_grad_circle(canvas, pos_x, pos_y, diameter, color_1, color_2, step_size, percent = 30):

    range_ = int(diameter/2 / 100 * percent)
    inc = (color_1 - color_2) / (range_//step_size)
    clr = color_1

    canvas.create_oval(pos_x, pos_y, pos_x + diameter, pos_y + diameter, fill=rgb_to_hex(color_1), outline='')
    for offset in range(0, range_, step_size):
        canvas.create_oval(pos_x + offset, pos_y + offset, pos_x + diameter - offset, pos_y + diameter - offset, fill=rgb_to_hex(clr), outline='')
        clr += inc
        clr = clr.clamp()

def draw_sun(canvas, pos_x, pos_y, diameter, step_size=4):
    sun_color_1 = Color([255, 194, 29])
    sun_color_2 = Color([255, 236, 98])

    draw_grad_circle(canvas, pos_x, pos_y, diameter, sun_color_1, sun_color_2, step_size)

def draw_moon(canvas, pos_x, pos_y, diameter, step_size=4):
    moon_color_1 = Color([214, 216, 211])
    moon_color_2 = Color([134, 155, 155])//2

    crater_color_1 = Color([227, 227, 221])
    crater_color_2 = Color([120, 120, 120])

    step_size = 4

    d = diameter//150

    draw_grad_circle(canvas, pos_x, pos_y, diameter, moon_color_1, moon_color_2, step_size, percent=120)
    draw_grad_circle(canvas, pos_x+diameter//2, pos_y+diameter//2, diameter//5, crater_color_1, crater_color_2, step_size=2, percent = 100)
    draw_grad_circle(canvas, pos_x+diameter//2-30*d, pos_y+diameter//2+20*d, diameter//10, crater_color_1, crater_color_2/4, step_size=2, percent = 100)
    draw_grad_circle(canvas, pos_x+diameter//2 - 30*d, pos_y+diameter//2 - 40*d, diameter//7, crater_color_1, crater_color_2, step_size=2, percent = 100)


def draw_dark_sphere(canvas, pos_x, pos_y, diameter, step_size=2):
    moon_color_2 = Color([214, 216, 211])
    moon_color_1 = Color([134, 155, 155])//2
    draw_grad_circle(canvas, pos_x, pos_y, diameter, moon_color_1, moon_color_2, step_size, percent=120)


def draw_clouds(canvas):
    offset = 20
    canvas.create_oval(10 + e.x, 10 + e.y, 500 + e.x, 250 + e.y, fill="#ffffff", outline='')
    canvas.create_oval(10 + e.x + 30, 10 + e.y + 10, 500 + e.x + 50, 250 + e.y - 10, fill=Color([250,250,255]).to_hex(), outline='')


def draw_circ_lines(canvas, inner_diameter, center_x, center_y, start, stop, thickness=88):
    diameter = inner_diameter
    radius = diameter // 2
    x_center, y_center = center_x + diameter//2, center_y + diameter//2
    for a in range(start, stop, 1):
        x = x_center + radius * math.cos(math.radians(a))
        y = y_center + radius * math.sin(math.radians(a))
        x1 = x_center + radius * math.cos(math.radians(a + thickness))
        y1 = y_center + radius * math.sin(math.radians(a + thickness))

        canvas.create_line(x, y, x1, y1, fill="white", width=1)


def cool_text_fx(canvas, text, sun_pos, sun_diam, text_pos, *, text_size=50, text_font='impact', line_color='white', text_color='white', line_width=2):
    pos_x, pos_y = sun_pos
    added = 20
    diameter = sun_diam + added
    #canvas.create_oval(pos_x - added, pos_y - added, pos_x + diameter, pos_y + diameter, fill="#ffffff", outline='')


    text_pos_x, text_pos_y = text_pos
    canvas.create_line(pos_x + diameter//2, pos_y + diameter//2, text_pos_x, text_pos_y, fill=line_color, width=line_width)

    canvas.create_text(text_pos_x, text_pos_y, anchor='w', font=(text_font, text_size), text=text, fill=text_color)


def parse_time(str_time):
    _h, _m = str_time.split(':')

    h, m = int(_h), int(_m)
    return h, m


def elevation(h):
    if 6 <= h <= 23:
        return 1 - ((h - 12) / 12)
    else:
        return 1 - ((h - 4) / 4)


def night(time):
    return 6 <= parse_time(time)[0] <= 23

def draw_sky(canvas, conditions, day_night, area_size = (1280, 720), step_size = 8):
    W, H = area_size

    colors = {
    'Sunny' : [
        Color([184, 216, 255]),
        Color([148, 188, 237])
    ],

    'Partly cloudy' : [
        Color([167, 153, 200]),
        Color([148, 188, 237])
    ],

    'Mist' : [
        Color([185, 204, 194]),
        Color([149, 168, 191])
    ],

    'Light rain' : [
        Color([180, 145, 209]),
        Color([105, 100, 210])
    ],

    'Overcast' : [
        Color([180, 145, 150]),
        Color([185, 180, 190])
    ],

    'Clear' : [
        Color([169, 153, 201]),
        Color([148, 188, 237])
    ],

    "Patchy light rain with thunder" : [
        Color([89, 88, 177]),
        Color([53, 62, 63])
    ],

    'Moderate rain' : [
        Color([89, 88, 177]),
        Color([53, 62, 63])
    ],

    "Moderate or heavy rain with thunder" : [
        Color([114, 71, 144]),
        Color([54, 66, 76])
    ],

    'night' : [
        Color([124, 143, 169]),
        Color([20, 36, 57])
    ]
    }

    if day_night == 'день':
        color_1, color_2 = colors[conditions]
    else:
        color_1, color_2 = colors['night']

    draw_grad(canvas, color_1, color_2, W, H, step_size=step_size)


def gui(canvas, width, height, weather_data):
    if 'error' in weather_data:
        color_1 = Color([100, 103, 109])
        color_2 = Color([7, 4, 1])
        draw_grad(canvas, color_1, color_2, 720, 720)
        cool_text_fx(canvas, 'Город не найден :(', (20, 20), 330, (220 + 330, 330//2))
        draw_dark_sphere(canvas, 20, 20, 330)
        return


    d = weather_data
    city_name = d['location']['name']
    country = d['location']['country']
    temp = d['current']['temp_c']
    feels_like = d['current']['feelslike_c']
    conditions = d['current']['condition']['text']
    day_night = ['ночь', 'день'][d['current']['is_day']]
    wind_speed = d['current']['wind_kph']
    visibility = d['current']['vis_km']
    time = d['location']['localtime'].split()[1]

    h, m = parse_time(time)
    sun_moon_h = 400 - 200 * elevation(h)
    #print(elevation(h))

    draw_sky(canvas, conditions, day_night, step_size = 10) # Drawing background

    cool_text_fx(canvas, f'Погода в {city_name} : {country}', (10, sun_moon_h), 300, (220 + 300, 300//2))
    cool_text_fx(canvas, f'{conditions}', (10, sun_moon_h), 300, (220 + 300, 300//2 + 100), text_size = 25)
    cool_text_fx(canvas, f'Температура: {temp}˚C / Ощущается как: {feels_like} ˚C', (10, sun_moon_h), 300, (220 + 300, 300//2 + 200), text_size = 25, text_color = 'white')
    cool_text_fx(canvas, f'Местное время: {time}', (10, sun_moon_h), 300, (220 + 300, 300//2 + 300), text_size = 20)
    cool_text_fx(canvas, f'Скорость ветра: {wind_speed} km/h', (10, sun_moon_h), 300, (220 + 300, 300//2 + 400), text_size = 20)

    #cool_text_fx('+30 C', (10, 10), 300, (220 + 250 + (1000/(screen_center_x - e.x)), 300 + (1000/(screen_center_y - e.y))))
    #sun_diam_range = list(range(100, 350, 20)) + list(range(350, 300, -20))
    #for d in sun_diam_range:
        #draw_sun(10, 10, d)
    if conditions in ["Partly cloudy", "Mist"]:
        draw_circ_lines(canvas, 330, 10, sun_moon_h, -70, 70, thickness = 88)
    if day_night == 'ночь':
        draw_moon(canvas, 10, sun_moon_h, 300)
    else:
        draw_sun(canvas, 10, sun_moon_h, 300)


if __name__ == '__main__':

    canvas = Canvas(root)
    canvas.grid(column=0, row=0, sticky=(N, W, E, S))

    #H, W = root.winfo_height(), root.winfo_width()
    #print(H, W)
    H, W = 720, 500
    draw_grad(canvas, (0, 0, 10), (247, 247, 240), H, W)

    #canvas.bind('<Motion>', _)
    canvas.bind('<1>', lambda e : gui(canvas, get_weather_data('tokyo')))#lambda e : draw_grad(Color.random(), Color.random(), H, W))
    root.mainloop()
