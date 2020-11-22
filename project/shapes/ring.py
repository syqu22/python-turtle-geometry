import turtle
from .shape import Shape

class Ring(Shape):
    def __init__(self, size, pos, color, fillcolor, range):
        super().__init__(size, pos, color, fillcolor)
        self.range = range
        
        #Draw desired shape using Bob from parent class
        self = super().getTurtle()  
        print(f"Bob {Shape.id} on duty, drawing Ring on {self.pos()}.")
        self.pensize(3)
        #First circle
        self.begin_fill()
        self.circle(range)
        self.goto(pos)
        self.up()
        self.left(90)
        self.forward(range*0.5)
        self.right(90)
        self.down()
        self.end_fill()
        #Second Circle inside First Circle
        self.color(color, "white")
        self.begin_fill()
        self.circle(range*0.5)
        self.end_fill()
