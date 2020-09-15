class Node:
    
    def __init__(self,dataval = None):
        
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    
    def __init__(self):
        
        self.headval = None
    
    def printval(self):
        x = self.headval
        while x is not None:
            print(x.dataval)
            x = x.nextval
    
    def insertnode(self):
        
        #Here we need to create a new node that we want to insert
        e4 = Node('Fri')
        self.headval.nextval = e4
        e4.nextval = e2

list1 = SLinkedList()
list1.headval = Node('Mon')
e2 = Node('Tue')
e3 = Node('Wed')
list1.headval.nextval = e2
e2.nextval = e3
list1.insertnode()
list1.printval()
