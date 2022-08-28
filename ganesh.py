#om ganesh
from turtle import *
speed(10)
ht()
setup(700,700)

#background
a=200
penup()
goto(0,-a)
pendown()
right(90)
begin_fill()
color('orange')
for i in range(6):
    circle(a/4,90)
    fd(a*0.3)
    circle(-a/3,45)
    left(150)
    circle(-a/3,45)
    fd(a*0.3)
    circle(a/4,90)
    right(180)
end_fill()
penup()
goto(0,-a*0.9)
seth(0)
pendown()
begin_fill()
color('gray')
circle(a*0.9)
end_fill()

#ganesh
color('black')
def f(x,y,a):
    penup()
    goto(x,y)
    seth(a)
    pendown()
for i in range(3):
    f(-i*5,110+i*15,0)
    for i in range(1,11):
        pensize(5+0.5*i)
        circle(100,3)
f(10,160,-90)
pensize(5)
circle(5)
f(40,100,-90)
for i in range(1,11):
    if i<3:
        pensize(8+i)
    else:
        pensize(14-i)
    circle(-300,3)
fd(10)
for i in range(8):
    if i<2:
        pensize(4+i)
    else:
        pensize(8-i)
    circle(70,3)
f(-5,20,-120)
for i in range(30):
    pensize(4+i*0.33)
    fd(2)
circle(60,150)
circle(10,30)
for i in range(10):
    pensize(13-i)
    circle(60,10)
for i in range(11):
    if i<5:
        pensize(4+i)
    else:
        pensize(13-i)
    circle(-30,-18)
f(55,35,30)
for i in range(1,11):
    pensize(i*0.8)
    fd(5)
circle(30,180)
for i in range(5):
    pensize(8-i)
    fd(3)
f(60,-21.92,-30)
for i in range(1,10):
    pensize(i)
    fd(3)
circle(-50,135)
fd(30)
for i in range(10):
    pensize(9-i*0.5)
    circle(-100,3)
for i in range(10):
    pensize(6-i*0.5)
    circle(15,15)
f(-30,-130,165)
for i in range(10):
    pensize(i*0.5)
    fd(5)
for i in range(10):
    pensize(5+i*0.5)
    circle(-60,15)
for i in range(10):
    pensize(10-i)
    circle(-20,18)
f(-55,20,30)
pensize(7)
fd(10)
right(90)
circle(-10,120)
circle(-20,120)
circle(70,10)
circle(-15,180)
f(-30,20,60)
for i in range(10):
    pensize(i*0.6)
    circle(50,3)
circle(30,30)
fd(60)
pensize(7)
circle(-23,240)
for i in range(5):
    pensize(7+i*0.5)
    circle(-5,18)
f(-5,90,0)
pensize(5)
circle(-50,30)
circle(-10,30)
fd(10)
f(-10,80,0)
pensize(3)
circle(-50,30)
pensize(6)
circle(-4)
pensize(3)
circle(-15,60)
f(0,45,-90)
begin_fill()
fd(5)
left(45)
circle(70,10)
circle(-1,155)
circle(-100,10)
circle(-1,120)
fd(13)
end_fill()


