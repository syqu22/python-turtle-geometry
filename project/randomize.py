from random import randint, choice

class Randomize:
    #Simple class with only static methods created for better space management
    
    #Randomizes color
    @staticmethod
    def color():  
        color = ["red","blue","green","orange","purple","pink", "grey", "brown", "lime", "gold","magenta","indigo","turquoise","silver"]
        return choice(color)

    #Randomizes position from x = (-400,400) and y = (-300,300)
    @staticmethod
    def pos():
        x = 400
        y = 300
        return randint(-x,x), randint(-y,y)

    #Randomizes size from 10 to 55
    @staticmethod
    def size():
        return randint(10, 55)
    
    #Randomizes pen size
    @staticmethod
    def pen_size():
        return randint(1,4)
    
    #Randomizes star size by picking a random number from the given sequence
    @staticmethod
    def star_size():
        sequence = [1,3.5,4,6]
        return choice(sequence)

    #Randomizes angle from 45 degrees to 270 degrees
    @staticmethod
    def angle():
        return randint(45,270)

    #Randomizes range from 20 to 150
    @staticmethod
    def range():
        return randint(20,150)
