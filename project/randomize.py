from random import randint

class Randomize:
    
    @staticmethod
    def color():  
        color = ["red","blue","green","orange","black","purple","pink", "grey", "white", "brown"]
        return color[randint(0,6)]

    @staticmethod
    def pos():
        x = 400
        y = 200
        return randint(-x,x), randint(-y,y)

    @staticmethod
    def size():
        return randint(10, 55)

    @staticmethod
    def angle():
        return randint(45,270)

    @staticmethod
    def range():
        return randint(20,150)