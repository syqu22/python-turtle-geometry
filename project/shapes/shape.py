import turtle

class Shape():
    #Create global variable to identify Bobs
    id = 0

    #Initiate Shape with basic info needed for Bob to work
    def __init__(self, size, pos, color, fillcolor, pen_size):
        self.size = size
        self.pos = pos
        self.color = color
        self.fillcolor = fillcolor
        self.pen_size = pen_size
        Shape.id += 1

    #Create a new turtle named Bob using given variables
    def getTurtle(self):
        bob = turtle.Turtle(visible=False)
        bob.color(self.color, self.fillcolor)
        bob.pensize(self.pen_size)
        bob.begin_fill()
        bob.speed(15)
        bob.up()        
        bob.setpos(self.pos)
        bob.down() 

        #Return Bob for later drawing
        return(bob)        
        