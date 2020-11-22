from shapes import scalene, ring, hexagon, star, heart
from randomize import Randomize as rand

def start_turtles():
    for i in range(4):
        #Scalenes
        scalene.Scalene(rand.size(), rand.pos(), rand.color(), rand.color(),rand.pen_size(), rand.angle())
        #Rings
        ring.Ring(rand.size(), rand.pos(), rand.color(), rand.color(),rand.pen_size(), rand.range())      
        #Hexagons
        hexagon.Hexagon(rand.size(), rand.pos(), rand.color(),rand.color(),rand.pen_size(), rand.angle(), rand.range())
        #Stars
        star.Star(rand.star_size(), rand.pos(), rand.color(),rand.color(),rand.pen_size(), rand.angle())
        #Hearts
        heart.Heart(rand.star_size(), rand.pos(), rand.color(),rand.color(),rand.pen_size(), rand.angle())

start_turtles()
