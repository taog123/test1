class  Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return "<node:{}>".format(self.data)
    __str__ = __repr__
class LinkList:
    def __init__(self):
        self.list = []
        self.head = None
        self.tail = None
    def append_node(self,node:Node):
        if self.head is None:
            self.head = node
        else:
            pre = self.tail
            pre.next = node
        self.tail = node
        self.list.append(node)
    def iternode(self):
        current = self.head
        while current:
            yield  current
            current = current.next
    def popnoed(self):
        if self.head is None :
            raise  NotImplementedError
        for node in  self.iternode():
            x = node.next
            if x is not None:
                xx = x.next
                if xx is None :
                    node.next = None
                    self.tail = node
                    return x
            else:
                self.head = None
                return  node
node1 = Node(3)
node2 = Node(5)
node3 = Node(6)
link = LinkList()
link.append_node(node1)
link.append_node(node2)
link.append_node(node3)
# link.popnoed()  #把最后一个抛出去
for node in link.iternode():
    print(node)