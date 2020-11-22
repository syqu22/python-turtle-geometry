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

    #Create a getter for turtle
    def get_turtle(self):
        bob = turtle.Turtle(visible=False)
        bob.color(self.color, self.fillcolor)
        bob.pensize(self.pen_size)
        bob.speed(20)
        
        #Very important is to make him stop drawing, move him to starting position then let him draw again
        bob.up()        
        bob.setpos(self.pos)
        bob.down()
        bob.begin_fill() 

        #Return Bob to use him for drawing
        return(bob)        
        