import turtle

class Shape():
    def __init__(self, size, pos, color, fillcolor):
        self.size = size
        self.pos = pos
        self.color = color
        self.fillcolor = fillcolor

    #Create a new turtle named Bob then return it for drawing purpose
    def getTurtle(self):
        bob = turtle.Turtle(visible=False)
        bob.color(self.color, self.fillcolor)
        bob.begin_fill()
        bob.speed(15)
        bob.up()        
        bob.setpos(self.pos)
        bob.down() 

        return(bob)        
        