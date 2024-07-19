import turtle
import random

colour = ['red','cyan','yellow','green','pink','purple' ]

bob = turtle.Turtle()
bob.speed(0)
def shift():
    bob.pu()
    bob.fd(200)
    bob.lt(90)
    bob.pd()
def square():
    bob.fillcolor(random.choice(colour))
    bob.begin_fill() 
    for i in range(4):
        bob.fd(100)
        bob.lt(90)
    bob.end_fill()
    
def grid():
    for i in range(4):
        square()
        shift()
def megaGrid():
    grid()
    bob.pu()
    bob.lt(180)
    bob.fd(200)
    bob.rt(180)
    bob.pd()
    grid()
    bob.pu()
    bob.rt(90)
    bob.fd(200)
    bob.lt(90)
    bob.pd()
    grid()
    bob.pu()
    bob.fd(200)
    bob.pd()
    grid()
    bob.lt(180)
    bob.fd(200)
    bob.rt(180)

megaGrid()



turtle.mainloop()