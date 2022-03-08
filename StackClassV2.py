import pickle
import os.path
"""
Add to the Stack class:
    A method to serialize a stack object
    A method to deserialize a stack object
    Define in the Stack class a class variable that will represent
    the maximum size a Stack may have
"""

class Stack:
    
    __MAX_SIZE=10000 # A class variable
    
    def __init__(self, size):
        if isinstance(size, int) and size > 0 and size < Stack.__MAX_SIZE:
            self.maxSize=size
            self.content=[]
        else:
            raise Exception("Wrong stack size given")
    
    def __repr__(self):
        return f"({len(self)}/{self.maxSize}) {self.content}"
    def __len__(self):
        return len(self.content)
    def __eq__(self, other):
        return self.maxSize == other.maxSize and self.content == other.content
    def __contains__(self, value): # in
        return value in self.content
    def __setattr__(self, name, value):
        if name not in self.__dict__:
            self.__dict__[name]=value
        else:
            raise Exception(f"{name} is a readonly attribute!")
    def push(self, value):
        if len(self) >= self.maxSize: #The stack is full
            raise Exception("Stack full!")
        else:
            self.content.append(value)
    def pop(self):
        if len(self)==0: # the stack is empty
            raise Exception("Stack empty!!")
        else:
            return self.content.pop()
    def peek(self):
        if len(self)==0: # the stack is empty
            raise Exception("Stack empty!!")
        else:
            return self.content[-1]
    def clear(self):
        self.content.clear()
    def isEmpty(self):
        return len(self)==0
    def extend(self, newSize):
        if isinstance(newSize, int) and newSize > self.maxSize and newSize <= Stack.__MAX_SIZE:
            self.__dict__["maxSize"]=newSize
        else:
            raise Exception("Wrong stack size given")
    def serialize(self,filename):
        with open(filename, "wb") as fic:
            pickle.dump(self,fic)
    @staticmethod 
    def deserialize(filename):
        if os.path.exists(filename):
            try:
                with open(filename, "rb") as fic:
                    temp=pickle.load(fic)
                    return temp
            except Exception:
                raise
        else:
            raise Exception(f"{filename} not found!")
    @staticmethod 
    def getMaxSize():
        return Stack.__MAX_SIZE   
       
if __name__ == "__main__":
   
    s1=Stack(10) # 10 is the maximum size of the Stack
    s1.push(24)
    s1.push(27)
    s1.push(29) # obj.method(arg1, arg2) -> method(obj, arg1, arg2)
    print("MAX SIZE is", Stack.getMaxSize())
    print("MAX SIZE is", s1.getMaxSize())
    print("MAX SIZE is", Stack._Stack__MAX_SIZE)
    print("MAX SIZE is", s1._Stack__MAX_SIZE)
    
    s1.serialize("data.pick")
    s4=Stack.deserialize("data.pick")
    print(s4)
    print(len(s1)) # 3
    print(len(s1)) # 3
    print(s1) # (3/10) [24,27,29]
    if 56 in s1:
        print("56 is in the Stack")
    else:
        print("56 is not in the Stack")
    top=s1.pop()
    print(top) # 29
    print(s1) # (2/10) [24,27]
    print(len(s1)) # 2
    top=s1.pop()
    print(top) # 27
    print(s1) # (1/10) [24]
    top=s1.peek()
    print(top) # 24
    print(s1) # (1/10) [24]
    s2=Stack(20) # 20 is the maximum size of the Stack
    s2.push(24)
    print(s2)
    print(s1==s2)
    s2.extend(25)
    print(s2)
    s2.clear()
    print(s2)
    
    # for e in s1:
    #     print(e)