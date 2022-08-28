from turtle import *
ht()
def f(x,y,a=0):
    penup()
    goto(x,y)
    seth(a)
    pendown()

def main(i):
    f(75*i,40*i,30)
    begin_fill()
    color('red')
    fd(25*i)
    circle(50*i,180)
    fd(150*i)
    circle(50*i,150)
    right(150)
    fd(25*i)
    circle(50*i,180)
    fd(150*i)
    circle(50*i,150)
    end_fill()
    color('white')
    f(-20*i,-50*i,90)
    begin_fill()
    fd(90*i)
    for j in range(3):
        right(120)
        fd(90*i)
    end_fill()
main(2)

