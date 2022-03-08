# Class attributes: class variable and class/static methods

class Point: # class Point(object):
    
    counter=0 # A "class variable" a "class data attribute" 
    
    def __init__(self, x, y):
        self.x=x # self.x is a "data attribute" or "instance variable" or "a field"
        self.y=y
        Point.counter += 1
    def __del__(self):
        print("__del__ called")
        Point.counter -= 1
    def __repr__(self): # __str__()
        return f"<{self.x},{self.y}>" # >= 3.6
    def __eq__(self, other): # __ne__
        return self.x==other.x and self.y==other.y
    def __add__(self, other): # + operator
        return Point(self.x+other.x, self.y+other.y)
    def __setattr__(self, name, value):
        if name not in ["x", "y"]:
            raise Exception("Wrong attribute name")
        if not isinstance(value, (int, float)):
            raise Exception("Wrong attribute value")
        self.__dict__[name]=value
    def __delattr__(self, name):
        raise Exception("You cannot delete an attribute")
    def distance(self, other):
        import math
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)
    def clear(self):
        self.x=self.y=0
    
#     @staticmethod
#     def parsePoint(param):
#         import re
#         regexp=re.compile(r"^<(\d+),(\d+)>$")
#         mo=regexp.search(param)
#         if mo:
#             return Point(int(mo[1]), int(mo[2]))
#         else:
#             raise Exception("This string is not a Point!")
            
# #    parsePoint=staticmethod(parsePoint)
        
    @classmethod 
    def parsePoint(cls, param):
        import re
        regexp=re.compile(r"^<(\d+),(\d+)>$")
        mo=regexp.search(param)
        if mo:
            return Point(int(mo[1]), int(mo[2]))
        else:
            raise Exception("This string is not a Point!")
            
#    parsePoint=classmethod(parsePoint)
    
def f():
    _=Point(0,0)
    print(f"Counter: {Point.counter}")
    print("The end")
    
if __name__ == "__main__":
    
    print(f"Counter: {Point.counter}")
    # print(Point.__dict__)
    p1=Point(2,3)
    p2=Point(5,7)
    
    print(f"Counter: {Point.counter}")
    print(f"Counter: {p1.counter}")
    # del p1
    f()
    print(f"Counter: {Point.counter}")
    print(p2) # <5,7>
    
    p3=Point.parsePoint("<23,67>")
    print(p3)


