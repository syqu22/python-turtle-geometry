import turtle
from .shape import Shape

class Hexagon(Shape):
    def __init__(self, size, pos, color, fillcolor, angle, range):
        super().__init__(size, pos, color, fillcolor)
        self.angle = angle
        self.range = range
 
        #Draw desired shape using Bob from parent class
        self = super().getTurtle()  
        print(f"Bob {Shape.id} on duty, drawing Hexagon on {self.pos()}.")
        self.pensize(3)
        self.begin_fill()  
        self.left(angle)      
        self.circle(range, steps=5)
        self.end_fill()