from .shape import Shape

class Heart(Shape):
    def __init__(self, size, pos, color, fillcolor, pen_size, angle):
        super().__init__(size, pos, color, fillcolor, pen_size)
        self.angle = angle
 
        #Get Bob from parent class
        self = super().get_turtle()
        print(f"Bob {Shape.id} on duty, drawing Heart on {self.pos()}.")

        self.left(angle)
        self.circle(size, extent=220)
        self.left(200)
        self.circle(size, extent=220)
        self.forward(size*2)
        self.goto(pos)
        self.end_fill()
        
            