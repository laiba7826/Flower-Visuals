from turtle import *
import colorsys
speed(0)
bgcolor("black")
colormode(1.0)  # Allows colors between 0 and 1
h = 0
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
        circle(40, 24)
done()
