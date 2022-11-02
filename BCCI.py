from turtle import *
speed(10)
ht()

def f(x,y,a=0):
    penup()
    goto(x,y)
    seth(0)
    pendown()
    
def dots(r,c,fill='#D6B268'):
    for i in range(c):
        color(fill)
        dot()
        penup()
        circle(r,360/c)
        pendown()
        
def star(r,fill='#D6B268'):
    penup()
    goto(0,-r)
    circle(r,180)
    pendown()
    color(fill)
    begin_fill()
    for i in range(5):
        left(72)
        fd(0.72656*r)
        right(72)
        fd(0.72656*r)
        left(72)
    end_fill()
f(0,-200)

#creating the outside circle
begin_fill()
circle(200)
fillcolor('#2255A4')
end_fill()
def design(r):
    circle(r,20)
    right(135)
    circle(r/3,60)
    right(135)
    circle(-r/3,45)
    left(135)
    circle(-r/3,60)
    left(33)
    circle(-79,-60)
    
circle(200,12.5)
for i in range(16):
    begin_fill()
    color('#D6B268')
    a=heading()
    p=pos()
    design(200)
    end_fill()
    seth(a)
    goto(p)
    circle(200,22.5)
    
f(0,-190)
pensize(5)
dots(190,60)

#creating inner circle
f(0,-100)
begin_fill()
fillcolor('#B3E3EE')
pensize(1)
circle(100)
end_fill()
star(100)

#creating dots for inner circle
f(0,-110)
pensize(5)
dots(110,40)
f(0,-140)

#typing the name
from circularletter import circular
circular('      board of control for cricket in india',25,140,9.5,270,3)

#heart Symbol
def heart(r):
    seth(45)
    circle(-r/2,180)
    fd(r)
    right(90)
    fd(r)
    circle(-r/2,180)
    
f(0,-140)
begin_fill()
heart(20)
end_fill()