from turtle import *
speed(10)
ht()
penup()
goto(0,-250)
seth(0)
pendown()
begin_fill()
color('#0c2c94')
for i in range(4):
    fd(50)
    circle(200,90)
    fd(50)
end_fill()
color('white')
begin_fill()
bk(30)
left(90)
circle(300,60)
fd(85)
right(60)
circle(-200,10)
right(105)
fd(80)
circle(-300,40)
circle(5,150)
circle(300,45)
fd(113)
right(95)
circle(-200,10)
right(75)
fd(150)
circle(10,140)
fd(125)
right(90)
fd(40)
right(90)
fd(125)
circle(10,140)
fd(150)
right(75)
circle(-200,10)
right(95)
fd(113)
circle(300,45)
circle(5,150)
circle(-300,40)
fd(80)
right(105)
circle(-200,10)
right(60)
fd(85)
circle(300,60)
right(90)
fd(25)
end_fill()
left(180)
pencolor('#8C8C8C')
pensize(15)
for i in range(4):
    fd(50)
    circle(200,90)
    fd(50)
