from .shape import Shape

class Heart(Shape):
    def __init__(self, size, pos, color, fillcolor, pen_size, angle):
        super().__init__(size, pos, color, fillcolor, pen_size)
        self.angle = angle
 
        #Draw desired shape using Bob from parent class
        self = super().getTurtle()  
        print(f"Bob {Shape.id} on duty, drawing Heart on {self.pos()}.")
        
        
            