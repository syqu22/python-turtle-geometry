from .shape import Shape

class Ring(Shape):
    def __init__(self, size, pos, color, fillcolor, pen_size, range):
        super().__init__(size, pos, color, fillcolor, pen_size)
        self.range = range
        
        #Get Bob from parent class
        self = super().getTurtle()  
        print(f"Bob {Shape.id} on duty, drawing Ring on {self.pos()}.")

        #Draw the outter circle first
        self.begin_fill()
        self.circle(range)
        self.goto(pos)
        self.up()
        self.left(90)
        self.forward(range*0.5)
        self.right(90)
        self.down()
        self.end_fill()
        #Draw the inner circle with filling it with white color so it can imitate empty circle
        self.color(color, "white")
        self.begin_fill()
        self.circle(range*0.5)
        self.end_fill()
