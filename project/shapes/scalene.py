import turtle
from .shape import Shape

class Scalene(Shape):
    def __init__(self, size, pos, color, fillcolor, angle):
        super().__init__(size, pos, color, fillcolor)
        self.angle = angle

        #Draw desired shape using Bob from parent class
        self = super().getTurtle()
        self.left(angle)
        self.forward(10 * size)
        self.left(15 * size)
        self.forward(14.5 * size)
        self.goto(pos)
        self.end_fill()