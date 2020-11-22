from .shape import Shape

class Scalene(Shape):
    def __init__(self, size, pos, color, fillcolor, pen_size, angle):
        super().__init__(size, pos, color, fillcolor, pen_size)
        self.angle = angle

        #Get Bob from parent class
        self = super().get_turtle()
        print(f"Bob {Shape.id} on duty, drawing Scalene on {self.pos()}.")

        #Do a basic drawing of Scalene
        self.left(angle)
        self.forward(5 * size)
        self.right(8 * size)
        self.forward(6 * size)
        self.goto(pos)
        self.end_fill()