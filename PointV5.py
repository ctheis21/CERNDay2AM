# Class attributes: class variable and class/static methods

class Point: # class Point(object):
    
    def __init__(self, x, y):
        self.__x=x # self.x is a "data attribute" or "instance variable" or "a field"
        self.__y=y

    def __repr__(self): # __str__()
        return f"<{self.__x},{self.__y}>" # >= 3.6
    def __eq__(self, other): # __ne__
        return self.__x==other.__x and self.__y==other.__y
    def __add__(self, other): # + operator
        return Point(self.__x+other.__x, self.__y+other.__y)
    
    def distance(self, other):
        import math
        return math.sqrt((other.__x-self.__x)**2 + (other.__y-self.__y)**2)
    def clear(self):
        self.__x=self.__y=0
        
    @property   
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self.__x=value
        else:
            raise Exception ("Wrong x value")
    
#   x=property(getX, setX) 

#   <=> 
    # x=property(getX)
    # x=x.setter(setX)
    
    def getY(self):
        return self.__y
    def setY(self, value):
        if isinstance(value, (int, float)):
            self.__y=value
        else:
            raise Exception ("Wrong y value")
            
    y=property(getY, setY)     
    
if __name__ == "__main__":
    p1=Point(2,3)
    print(p1)
    p1.x=23
    print(p1.x)
    p1.y=56
    print(p1.y)
   
    
    


