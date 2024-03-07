class linkedListNode:
    def __init__(self, data=None, next_index=None):
        self.data = data
        self.next_index = next_index

class linkedList:
    def __init__(self, size):
        self.my_linked_list = [linkedListNode() for _ in range(size)]
        self.start_pointer = -1
        self.heap_start_pointer = 0
    def add_node_after(self, data, target_index):
        if self.heap_start_pointer <len(self.my_linked_list):
            new_index = self.heap_start_pointer
            self.heap_start_pointer += 1
            new_node = linkedListNode(data)  # Set data for the new node
            