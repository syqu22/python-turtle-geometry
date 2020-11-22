from shapes import scalene, ring, hexagon
from randomize import Randomize as rand

def start_turtles():
    for i in range(4):
        #Scalenes
        scalene.Scalene(rand.size(), rand.pos(), rand.color(), rand.color(), rand.angle())
        #Rings
        ring.Ring(rand.size(), rand.pos(), rand.color(), rand.color(), rand.range())      
        #Hexagons
        hexagon.Hexagon(rand.size(), rand.pos(), rand.color(),rand.color(), rand.angle(), rand.range())


start_turtles()
