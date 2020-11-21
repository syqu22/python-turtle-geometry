import turtle

class Scalene:
    def __init__(self, size, pos, color, fillcolor, angle, speed):
        #Setting turtle
        self = turtle.Turtle()
        self.hideturtle()
        self.color(color, fillcolor)
        self.begin_fill()
        self.speed(speed)
        self.up()        
        self.setpos(pos)
        self.left(angle)
        self.down()

        #Drawing      
        self.forward(10 * size)
        self.left(15 * size)
        self.forward(14.5 * size)
        self.goto(pos)
        self.end_fill()