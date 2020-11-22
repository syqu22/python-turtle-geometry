from shapes import scalene, ring
from random import randint

color = ["red","blue","green","orange","black","purple","pink"]

def randcolor():  
    pass

def randpos():
    pass

def start_turtles(code=0):
    #Invoke Scalenes 1
    if(code == 0 or code == 1):
        scalene.Scalene(30, (0,50),"pink","black", 90)
        scalene.Scalene(20, (450,-60),"blue","green", 200)
        scalene.Scalene(17, (-300,25),"black","white", 45)
        scalene.Scalene(9, (-30,-300),"red","yellow", 350)

    #Invoke Rings 2
    if(code == 0 or code == 2):
        ring.Ring(10, (45,90),"black","white", 40)
        ring.Ring(22, (152,250),"orange","purple", 15)
        ring.Ring(15, (110,60),"red","pink", 90)
        ring.Ring(4, (200,10),"green","grey", 40)

start_turtles(2)

while True:
    pass