from turtle import *
k = 15
tracer(0)    #отключить анимацию

begin_fill()
for i in range(5):
    circle(0, 0, 5, 180)
    circle
end_fill()
up()

count = 0
canvas = getcanvas()
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x*k, y*k, x*k, y*k) == (5,):
            count += 1
print(count)