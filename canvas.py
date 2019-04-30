from tkinter import *
from tkinter import ttk
import random
import math
import gettext

import locale

try:
    cfg = open('lang.cfg', 'r')
except:
    lang = locale.getdefaultlocale()
    if lang[0].startswith('en'):
        sys_lang = 'EN'
    if lang[0].startswith('ru'):
        sys_lang = 'RU'    
else:
    sys_lang = cfg.readline().split(':')[1]
    
    

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
        r, g, b = self.rgb
        def clamp_one(v):
            if v >= 255:
                v = 255
            if v <= 0:
                v = 0
            return v

        r = clamp_one(r)
        g = clamp_one(g)
        b = clamp_one(b)

        return Color([r, g, b])

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


def draw_grad(canvas, start_color, end_color, W=1280, H=800, step_size=20):
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


def cool_text_fx(canvas, text, sun_pos, sun_diam, text_pos, *, text_size=50, text_font='avenir next', line_color='white', text_color='white', line_width=2):
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

def translate(conditions, lang):
    
    translate = {
        'Sunny' : 'Солнечно',
        'Partly cloudy' : 'Частичная облачность',
        'Mist' : 'Туман',
        'Light rain' : 'Легкий дождь',
        'Overcast' : 'Пасмурно',
        'Clear' : 'Ясно',
        "Patchy light rain with thunder" : 'Местами легкий дождь с грозой',
        'Moderate rain' : 'Умеренный дождь',
        "Moderate or heavy rain with thunder" : 'Умеренный-сильный дождь с грозой',
        'city not found' : 'город не найден',
        'night' : 'ночь',
        'day' : 'день',
        'Weather in' : 'Погода в',
        'Temperature' : 'Температура',
        'Feels like' : 'Ощущается как',
        'Windspeed' : 'Скорость ветра',
        'Local time' : 'Местное время',
    }
    
    if lang == 'RU' and conditions in translate:
        return translate[conditions]
    else:
        return conditions
    

def draw_sky(canvas, conditions, day_night, area_size = (720, 1080), step_size = 8):
    H, W = area_size

    colors = {
    'Sunny' : [
        Color([114, 202, 240]),
        Color([234, 67, 38])
    ],

    'Partly cloudy' : [
        Color([103, 116, 222]),
        Color([85, 247, 173])
    ],

    'Mist' : [
        Color([185, 204, 194]),
        Color([149, 168, 191])
    ],

    'Light rain' : [
        Color([221, 174, 211]),
        Color([221, 174, 211])
    ],

    'Overcast' : [
        Color([113, 2, 116]),
        Color([181, 57, 62])
    ],

    'Clear' : [
        Color([26, 157, 136]),
        Color([2, 171, 109])
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


    try:
        color_1, color_2 = colors[conditions]
    except:
        color_1 = Color([100, 103, 109])
        color_2 = Color([7, 4, 1])
    if day_night == 'night':
        color_n1, color_n2 = colors['night']
        color_1 = (color_1 + color_n1) // 2
        color_2 = (color_2 + color_n2) // 2

    draw_grad(canvas, color_1, color_2, W, H, step_size=step_size)
    if "thunder" in conditions:
        draw_lighting(canvas, H, W)



def draw_lighting_from(canvas, x, y, W, H, steps = 2, depth=8):
    if random.random() >= 0.3:
        return

    if depth <= 0:
        return

    x1, y1 = x, y

    for branches in range(random.choice(list(range(4)))):
        line_width = 1
        line_color = Color([171, 194, 253])

        y1 = math.floor(y + random.random() * 200)
        x1 = math.floor(x + (random.random() - 0.5) * 400)
        dec = (line_width - 1) / steps
        canvas.create_line(x, y, x1, y1, fill=line_color.to_hex(), width=line_width)

        draw_lighting_from(canvas, x1, y1, W, H, steps, depth=depth-1)


def draw_lighting(canvas, W, H, steps = 2):
    if random.random() <= 0.5:
        return

    x, y = random.randint(10, W), 0
    x1, y1 = x, y

    for segments in range(20):
        line_width = 2
        line_color = Color([171, 194, 253])
        x, y = x1, y1
        for branches in range(random.choice(list(range(4)))):

            y1 = math.floor(y + random.random() * 400)
            x1 = math.floor(x + (random.random() - 0.5) * 400)
            dec = (line_width - 1) / steps
            for i in range(steps):
                canvas.create_line(x, y, x1, y1, fill=line_color.to_hex(), width=line_width)
                line_width = math.ceil(line_width - dec)
                line_color = (line_color + Color([90, 90, 90])).clamp()
            draw_lighting_from(canvas, x1, y1, W, H, steps)


def gui(canvas, W, H, weather_data):

    if W >= 1410:
        text_dist = H // 8
        distance = W // 5
        icon_size = 330
        circ_d = 33
        ets = 40

    elif W <= 900 and H <= 500:
        text_dist = 50
        icon_size = 100
        distance = 80
        circ_d = 10
        ets = 20

    elif W <= 1400 and H <= 700:
        text_dist = 70
        icon_size = 200
        distance = 100
        circ_d = 20
        ets = 25
    else:
        text_dist = 100
        icon_size = 300
        distance = 220
        circ_d = 30
        ets = 30

    if 'error' in weather_data:
        color_1 = Color([100, 103, 109])
        color_2 = Color([7, 4, 1])
        draw_grad(canvas, color_1, color_2, H, W)
        cool_text_fx(canvas, _('City not found :('), (20, 20), icon_size, (distance + icon_size, icon_size//2), text_size = ets)
        draw_dark_sphere(canvas, 20, 20, icon_size)
        return


    d = weather_data
    city_name = d['location']['name']
    country = d['location']['country']
    temp = d['current']['temp_c']
    feels_like = d['current']['feelslike_c']
    conditions = d['current']['condition']['text']
    day_night = ['night', 'day'][d['current']['is_day']]
    wind_speed = d['current']['wind_kph']
    visibility = d['current']['vis_km']
    time = d['location']['localtime'].split()[1]

    h, m = parse_time(time)
    sun_moon_h = 400 - 200 * elevation(h)
    #print(elevation(h))

    draw_sky(canvas, conditions, day_night, area_size = (H, W), step_size = 10) # Drawing background
    city_name_text = _('Weather in')
    cool_text_fx(canvas, f'{city_name_text} {city_name} : {country}', (10, sun_moon_h), icon_size, (distance + icon_size, icon_size//2), text_size = 25)
    cool_text_fx(canvas, f'{conditions}', (10, sun_moon_h), icon_size, (distance + icon_size, icon_size//2 + text_dist), text_size = 25)
    temp_text = _('Temperature')
    cool_text_fx(canvas, f'{temp_text}: {temp} ˚C', (10, sun_moon_h), icon_size, (distance + icon_size, icon_size//2 + 2*text_dist), text_size = 25, text_color = 'white')
    feels_like_text = _('Feels like')
    cool_text_fx(canvas, f'{feels_like_text}: {feels_like} ˚C', (10, sun_moon_h), icon_size, (distance + icon_size, icon_size//2 + 3*text_dist), text_size = 25)
    time_text = _('Local time')
    cool_text_fx(canvas, f'{time_text}: {time}', (10, sun_moon_h), icon_size, (distance + icon_size, icon_size//2 + 4*text_dist), text_size = 20)
    wind_speed_text = _('Windspeed')
    cool_text_fx(canvas, f'{wind_speed_text}: {wind_speed} km/h', (10, sun_moon_h), icon_size, (distance + icon_size, icon_size//2 + 5*text_dist), text_size = 20)

    #cool_text_fx('+30 C', (10, 10), 300, (220 + 250 + (1000/(screen_center_x - e.x)), 300 + (1000/(screen_center_y - e.y))))

    if conditions in ["Partly cloudy", "Mist"]:
        draw_circ_lines(canvas, icon_size + circ_d, 10, sun_moon_h, -70, 70, thickness = 88)

    if day_night == 'night':
        draw_moon(canvas, 10, sun_moon_h, icon_size)
    else:
        draw_sun(canvas, 10, sun_moon_h, icon_size)

import os.path

datapath = os.path.dirname(sys.argv[0])
gettext.install('canvas', datapath, names=("ngettext",))

if __name__ == '__main__':

    canvas = Canvas(root)
    canvas.grid(column=0, row=0, sticky=(N, W, E, S))

    #H, W = root.winfo_height(), root.winfo_width()
    #print(H, W)
    H, W = 720, 500
    draw_grad(canvas, (0, 0, 10), (247, 247, 240), W, H)

    canvas.bind('<Motion>', lambda e : gui(canvas, 1600, 1200, get_weather_data('brescia')))
    canvas.bind('<1>', lambda e : gui(canvas, 1600, 1200, get_weather_data('tokyo')))#lambda e : draw_grad(Color.random(), Color.random(), H, W))
    root.mainloop()

    
