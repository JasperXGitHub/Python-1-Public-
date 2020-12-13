import turtle as t
t.penup()
t.shape('turtle')
t.bgcolor('blue')
t.speed('fast')

def rect(horizontal,vertical,color):
    t.pendown()
    t.color(color)
    t.begin_fill()
    for counter in range (0,2):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
#feet
t.goto(-100,-150)
rect(50,20,'red')
t.goto(-30,-150)
rect(50,20,'red')
#leg
t.goto(-25,-50)
rect(15,100,'yellow')
t.goto(-70,-50)
rect(15,100,'yellow')

#body
t.goto(-90,100)
rect(100,150,'tan')

#arms
t.goto(-150,70)
rect(60,15,'purple')
t.goto(-150,110)
rect(15,40,'purple')

t.goto(10,70)
rect(60,15,'purple')
t.goto(55,110)
rect(15,40,'purple')


#neck
t.goto(-50,120)
rect(15,20,'yellow')

t.hidetutle()
