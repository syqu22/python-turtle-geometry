import turtle
from .shape import Shape

class Star(Shape):
    def __init__(self, size, pos, color, fillcolor, angle):
        super().__init__(size, pos, color, fillcolor)
        self.angle = angle
 
        #Draw desired shape using Bob from parent class
        self = super().getTurtle()  
        print(f"Bob {Shape.id} on duty, drawing Star on {self.pos()}.")
        self.begin_fill()
        self.left(angle)
        for i in range(5):
            self.up()
            self.forward(100 * size)
            self.right(144 * size)
            self.down()
        self.end_fill()
            