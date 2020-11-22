from shapes import scalene, ring
from random import randint

def randcolor():  
    color = ["red","blue","green","orange","black","purple","pink", "grey", "white"]
    return color[randint(0,6)]

def randpos():
    x = 350
    y = 350

    return randint(-x,x), randint(-y,y)

def randsize():
    return randint(10, 40)

def randangle():
    return randint(90,270)

def start_turtles():
        #Scalenes
        scalene.Scalene(randsize(), randpos(),randcolor(),randcolor(), randangle())
        scalene.Scalene(randsize(), randpos(),randcolor(),randcolor(), randangle())
        scalene.Scalene(randsize(), randpos(),randcolor(),randcolor(), randangle())
        scalene.Scalene(randsize(), randpos(),randcolor(),randcolor(), randangle())
        #Rings
        #ring.Ring(10, (45,90),"black","white", 40)
        #ring.Ring(22, (152,250),"orange","purple", 15)
        #ring.Ring(15, (110,60),"red","pink", 90)
        #ring.Ring(4, (200,10),"green","grey", 40)


start_turtles()
