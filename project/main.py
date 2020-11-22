from shapes import scalene, ring
from randomize import Randomize as rand

def start_turtles():
        #Scalenes
        scalene.Scalene(rand.size(), rand.pos(),rand.color(),rand.color(), rand.angle())
        scalene.Scalene(rand.size(), rand.pos(),rand.color(),rand.color(), rand.angle())
        scalene.Scalene(rand.size(), rand.pos(),rand.color(),rand.color(), rand.angle())
        scalene.Scalene(rand.size(), rand.pos(),rand.color(),rand.color(), rand.angle())
        #Rings
        ring.Ring(rand.size(), rand.pos(),rand.color(),rand.color(), rand.range())
        ring.Ring(rand.size(), rand.pos(),rand.color(),rand.color(), rand.range())
        ring.Ring(rand.size(), rand.pos(),rand.color(),rand.color(), rand.range())
        ring.Ring(rand.size(), rand.pos(),rand.color(),rand.color(), rand.range())


start_turtles()
