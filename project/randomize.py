from random import randint, choice

class Randomize:
    
    @staticmethod
    def color():  
        color = ["red","blue","green","orange","black","purple","pink", "grey", "white", "brown"]
        return color[randint(0,6)]

    @staticmethod
    def pos():
        x = 400
        y = 350
        return randint(-x,x), randint(-y,y)

    @staticmethod
    def size():
        return randint(10, 55)
    
    @staticmethod
    def pen_size():
        return randint(1,2)
    
    @staticmethod
    def star_size():
        sequence = [1,3.5,4,6]
        return choice(sequence)

    @staticmethod
    def angle():
        return randint(45,270)

    @staticmethod
    def range():
        return randint(20,150)
