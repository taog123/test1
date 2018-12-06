import random
class num:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def bbb(self):
        d=[]
        for i in range(self.a):
            e=random.randint(self.b,self.c)
            d.append(e)
        print(d)
        for i in range(0,self.a,2):
            g=d[i],d[i+1]
            print(g)
f=num(20,1,100)
f.bbb()
