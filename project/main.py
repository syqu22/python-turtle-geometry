from shapes import scalene, ring, hexagon, star, heart
from randomize import Randomize as rand

def start_turtles():
    for i in range(4):
        #Scalene
        scalene.Scalene(rand.size(), rand.pos(), rand.color(), rand.color(),rand.pen_size(), rand.angle())
        #Ring
        ring.Ring(rand.size(), rand.pos(), rand.color(), rand.color(),rand.pen_size(), rand.range())      
        #Hexagon
        hexagon.Hexagon(rand.size(), rand.pos(), rand.color(),rand.color(),rand.pen_size(), rand.angle(), rand.range())
        #Star
        star.Star(rand.star_size(), rand.pos(), rand.color(),rand.color(),rand.pen_size(), rand.angle())
        #Heart
        heart.Heart(rand.star_size(), rand.pos(), rand.color(),rand.color(),rand.pen_size(), rand.angle())

start_turtles()
