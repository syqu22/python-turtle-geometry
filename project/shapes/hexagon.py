from .shape import Shape

class Hexagon(Shape):
    def __init__(self, size, pos, color, fillcolor, pen_size, angle, range):
        super().__init__(size, pos, color, fillcolor, pen_size)
        self.angle = angle
        self.range = range
 
        #Get Bob from parent class
        self = super().get_turtle()
        print(f"Bob {Shape.id} on duty, drawing Hexagon on {self.pos()}.")

        #Do a basic drawing of Hexagon
        self.left(angle)      
        self.circle(range, steps=5)
        self.end_fill()