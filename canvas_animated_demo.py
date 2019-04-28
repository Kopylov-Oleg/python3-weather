from tkinter import *
from tkinter import ttk
import random

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
        return Color(map(lambda x : x // k, self.rgb))

    def __truediv__(self, k):
        return Color(map(lambda x : x / k, self.rgb))

    def to_hex(self):
        return '#' + ''.join('{:02X}'.format(a) for a in self.rgb)

    def __str__(self):
        return '(' + ', '.join(list(map(str, self.rgb))) + ')'


def rgb_to_hex(rgb):
    return rgb.to_hex()


def draw_grad(start_color, end_color, H=200, W=400, step_size=20):
    start_color = Color(start_color)
    end_color = Color(end_color)
    value = start_color
    steps = H // step_size
    inc = (start_color - end_color) / steps

    for y in range(0, H, step_size):
        for x in range(0, W, step_size):
            #print(value)
            #canvas.create_rectangle(i, j, i+step_size, j+step_size, outline='', fill=rgb_to_hex(value))
            canvas.create_line(x, y, x + W, y, fill=rgb_to_hex(value.clamp()),width=step_size)

        value += inc

    #draw_moon(100, 100, 300)


def draw_grad_circle(pos_x, pos_y, diameter, color_1, color_2, step_size, percent = 30):

    range_ = int(diameter/2 / 100 * percent)
    inc = (color_1 - color_2) / (range_//step_size)
    clr = color_1

    canvas.create_oval(pos_x, pos_y, pos_x + diameter, pos_y + diameter, fill=rgb_to_hex(color_1), outline='')
    for offset in range(0, range_, step_size):
        canvas.create_oval(pos_x + offset, pos_y + offset, pos_x + diameter - offset, pos_y + diameter - offset, fill=rgb_to_hex(clr), outline='')
        clr += inc
        clr = clr.clamp()

def draw_sun(pos_x, pos_y, diameter, step_size=4):
    sun_color_1 = Color([255, 194, 29])
    sun_color_2 = Color([255, 236, 98])

    draw_grad_circle(pos_x, pos_y, diameter, sun_color_1, sun_color_2, step_size)

def draw_moon(pos_x, pos_y, diameter, step_size=4):
    moon_color_1 = Color([214, 216, 211])
    moon_color_2 = Color([134, 155, 155])//2

    crater_color_1 = Color([227, 227, 221])
    crater_color_2 = Color([120, 120, 120])

    step_size = 4

    d = diameter//150

    draw_grad_circle(pos_x, pos_y, diameter, moon_color_1, moon_color_2, step_size, percent=120)
    draw_grad_circle(pos_x+diameter//2, pos_y+diameter//2, diameter//5, crater_color_1, crater_color_2, step_size=2, percent = 100)
    draw_grad_circle(pos_x+diameter//2-30*d, pos_y+diameter//2+20*d, diameter//10, crater_color_1, crater_color_2/4, step_size=2, percent = 100)
    draw_grad_circle(pos_x+diameter//2 - 30*d, pos_y+diameter//2 - 40*d, diameter//7, crater_color_1, crater_color_2, step_size=2, percent = 100)


def draw_dark_sphere(pos_x, pos_y, diameter, step_size=2):
    moon_color_2 = Color([214, 216, 211])
    moon_color_1 = Color([134, 155, 155])//2
    draw_grad_circle(pos_x, pos_y, diameter, moon_color_1, moon_color_2, step_size, percent=120)



def cool_text_fx(text, sun_pos, sun_diam, text_pos):
    pos_x, pos_y = sun_pos
    added = 20
    diameter = sun_diam + added
    canvas.create_oval(pos_x - added, pos_y - added, pos_x + diameter, pos_y + diameter, fill="#ffffff", outline='')

    text_pos_x, text_pos_y = text_pos
    canvas.create_line(pos_x + diameter//2, pos_y + diameter//2, text_pos_x, text_pos_y, fill="#ffffff", width=5)

    canvas.create_text(text_pos_x, text_pos_y, anchor='w', font=('impact', 50), text=text, fill='#ffffff')


def beautiful_appearance(e):
    screen_center_x = 200
    screen_center_y = 500

    color_1 = Color([103, 160, 205])
    color_2 = Color([249, 255, 237])
    draw_grad(color_1, color_2, 1280, 720, step_size = 20)

    cool_text_fx('Sunny!', (10, 10), 300, (220 + 300 + (1000/(screen_center_x - e.x)), 300//2 + (1000/(screen_center_y - e.y))))

    cool_text_fx('+30 C', (10, 10), 300, (220 + 250 + (1000/(screen_center_x - e.x)), 300 + (1000/(screen_center_y - e.y))))
    #sun_diam_range = list(range(100, 350, 20)) + list(range(350, 300, -20))
    #for d in sun_diam_range:
        #draw_sun(10, 10, d)

    draw_sun(10, 10, 300, step_size = 10)







canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

#H, W = root.winfo_height(), root.winfo_width()
#print(H, W)
H, W = 1280, 720
draw_grad((0, 0, 10), (247, 247, 240), H, W)

canvas.bind('<Motion>', beautiful_appearance) #lambda e : print(e.x))
canvas.bind('<1>', beautiful_appearance)#lambda e : draw_grad(Color.random(), Color.random(), H, W))
root.mainloop()
