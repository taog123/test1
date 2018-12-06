class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __hash__(self):
        return hash((self.x,self.y))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __add__(self, other):
        return (self.x + other.x,self.y + other.y)
    def __sub__(self, other):
        return (self.x - other.x,self.y - other.y)
    def __lt__(self, other):
        return (self.x < other.x and self.y < other.y)
a=Point(2,3)
b=Point(2,3)

print(hash(a))
print(hash(b))
print(a is b)
print(a.__eq__(b))
print(a == b)
print(a+b)
print(a-b)
print(a<b)


# class Test:
#     def __init__(self,item):
#         self.item = item
#     def __len__(self):
#         return len(self.item)
# f=Test([1,2,3,4,5])
# print(len(f))

# class Foo:
#     def __init__(self, item):
#         self.item = item
#
#     def __getitem__(self, item):
#         # print('getitem is run')
#         return self.item[item]
#
#
# f1=Foo(['Charm', 'Night', '2018', '加油'])
# print(f1[0])