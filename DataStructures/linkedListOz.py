class linkedList:
    class Node:
        def __init__(self, data, pointer = None):
            self.data, self.pointer = data, pointer
    def __init__(self):
        self.start = None
    def add(self, item):
        newNode = self.Node(self, item)
        currentNode = self.start
        if not currentNode or item < currentNode.data:
            newNode.pointer, self.start = currentNode, newNode
        else: 
            while currentNode and currentNode.data < item:
                previousNode, currentNode = currentNode, currentNode.pointer
                newNode.pointer, previousNode.pointer = previousNode.pointer, new_node
        return True
    def delete(self, item):
        currentNode =self.start
        if currentNode:
            if item == currentNode.data:
                self.start = currentNode.pointer
            else:
                while currentNode and item != currentNode.data:
                    previousNode, currentNode = currentNode, currentNode.pointer
                if currentNode:
                    previousNode.pointer = currentNode.pointer
    def output(self):
        items, currentNode = [], self.start
        while currentNode:
            items.append(currentNode.data)
            currentNode = currentNode.pointer
            return items

items = ["a","b","c","d","e"]
linked_List = linkedList
index1 = 0
for _ in range(len(items)):
    linked_List.add(items[index1])
    index1 += 1
print("original linked list:", linked_List.output())
linked_List.delete("b")
print("linked list:",linked_List.output())
linked_List.add("f")
print("linked list:", linked_List.output())
