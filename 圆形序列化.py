import math
import json
class Shape:
    def __init__(self,n):
        self.n=n
    def area(self):
        raise type-error
class Circular(Shape):
    def area(self):
        area=math.pi*self.n**2
        return area
    def jasoning(self,jason):
        c=json.dumps(self.__dict__)
        return c

b=Circular(3)    #实例化圆形
c=b.jasoning('jason')
print(c)