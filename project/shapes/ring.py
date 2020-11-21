import turtle

class Ring:
    def __init__(self, size, pos, color, fillcolor, range, speed):
        #Setting turtle
        self = turtle.Turtle()
        self.hideturtle()
        self.color(color, fillcolor)
        self.begin_fill()
        self.speed(speed)
        self.up()        
        self.setpos(pos)
        self.down()
        self.pensize(3)

        #Drawing      
        self.circle(range*1.5)
        self.goto(pos)
        self.up()
        self.left(90)
        self.forward(range*3)
        self.down()
        self.circle(range)