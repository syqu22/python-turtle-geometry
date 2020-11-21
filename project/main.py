from shapes import scalene, ring
from random import randint

color = ["red","blue","green","orange","black","purple","pink"]

def randcolor():
    pass

def randpos():
    pass

def start_turtles(speed=25):
    #Invoke Scalenes
    scalene.Scalene(30, (0,50),"pink","black", 90, speed)
    scalene.Scalene(20, (450,-60),"blue","green", 200, speed)
    scalene.Scalene(17, (-300,25),"black","white", 45, speed)
    scalene.Scalene(9, (-30,-300),"red","yellow", 350, speed)

    #Invoke Rings
    #ring.Ring(10, (45,90),"orange","purple",40, speed)
    #ring.Ring(22, (152,250),"orange","purple",15, speed)
    #ring.Ring(15, (110,60),"orange","purple",90, speed)
    #ring.Ring(4, (200,10),"orange","purple",40, speed)

start_turtles()