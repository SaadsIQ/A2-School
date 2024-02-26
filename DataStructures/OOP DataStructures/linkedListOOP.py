class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            
