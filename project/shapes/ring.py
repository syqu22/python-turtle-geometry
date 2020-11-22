import turtle
from .shape import Shape

class Ring(Shape):
    def __init__(self, size, pos, color, fillcolor, range):
        super().__init__(size, pos, color, fillcolor)
        self.range = range
        
        #Draw desired shape using Bob from parent class
        self = super().getTurtle()  
        self.pensize(2)
        self.circle(range*1.5)
        self.goto(pos)
        self.up()
        self.left(90)
        self.forward(range*4)
        self.down()
        self.circle(range)