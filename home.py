from turtle import*
setup(900,700)
speed(10)
ht()
x,y=-270,-240
def move(x,y,a=0):
    '''
        To move the point to x,y and seting the turtle angle with a
    '''
    penup()
    goto(x,y)
    seth(a)
    pendown()

def rectangle(l,b,c=0,fill='white'):
    '''
        To form a rectangle with length l and breadth b and edge curve radius c
    '''
    begin_fill()
    fillcolor(fill)
    for i in range(2):
        fd(l)
        circle(c,90)
        fd(b)
        circle(c,90)
    end_fill()

def boxes(l,b,cl,cb,ps,pc,fill='black'):
    p=pensize()
    c=pencolor()
    pensize(ps)
    pencolor(pc)
    bl=l/cl
    bb=b/cb
    for i in range(cb):
        for j in range(cl):
            rectangle(bl,bb,0,fill)
            fd(bl)
        bk(l)
        left(90)
        fd(bb)
        right(90)
    pensize(p)
    pencolor(c)

def triangle(s,fill=color()):
    begin_fill()
    fillcolor(fill)
    for i in range(3):
        fd(200)
        left(120)
    end_fill()

def trapboxs(l,b,cl,cb,fill):
    begin_fill()
    fillcolor(fill)
    for i in range(cb):
        for k in range(2):
            fd(l)
            left(120)
            fd(b/cb)
            left(60)
        left(120)
        fd(b/cb)
        right(120)
    right(60)
    fd(b)
    left(60)
    for i in range(cl-1):
        for k in range(2):
            fd(l/cl)
            left(120)
            fd(b)
            left(60)
        fd(l/cl)
    end_fill()
#main       
move(x,y)
rectangle(200,250,0,'#6CA1AD')
#door
move(x+50,y)
rectangle(50,130,5,'#F2AF0E')
#main window
move(x+110,y+40)
boxes(80,80,2,2,5,'brown','white')
#top
move(x,y+250)
triangle(200,'#C26C11')
move(x+100,y+270)
begin_fill()
fillcolor('white')
circle(25)
end_fill()
#right wall
move(x+200,y)
rectangle(350,250,0,'#BF9564')
#right wall windows
move(x+250,y+40)
boxes(80,120,2,3,5,'brown','white')
move(x+420,y+40)
boxes(80,120,2,3,5,'brown','white')
#right top
move(x+200,y+250)
trapboxs(350,200,20,10,'#8FBFA9')
#steps
move(x+30,y)
boxes(90,-10,1,1,1,'#727278','#727278')
trapboxs(90,-20,1,2,'#727278')
move(-250,225)
begin_fill()
color('red')
for i in range(36):
    circle(50,10)
    right(90)
    if i%2==0:
        fd(20)
        bk(20)
    else:
        fd(10)
        bk(10)
    left(90)
end_fill()
bgcolor('yellow')
