import turtle

class Shape():
    id = 0

    def __init__(self, size, pos, color, fillcolor, pen_size):
        self.size = size
        self.pos = pos
        self.color = color
        self.fillcolor = fillcolor
        self.pen_size = pen_size
        Shape.id += 1

    #Create a new turtle named Bob then return it for drawing purposes
    def getTurtle(self):
        bob = turtle.Turtle(visible=False)
        bob.color(self.color, self.fillcolor)
        bob.pensize(self.pen_size)
        bob.begin_fill()
        bob.speed(15)
        bob.up()        
        bob.setpos(self.pos)
        bob.down() 

        return(bob)        
        