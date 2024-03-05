class LinkedListNode:
    def __init__(self, data=None, next_index=None):
        self.data = data
        self.next_index = next_index

class LinkedList:
    def __init__(self, size):
        self.my_linked_list = [LinkedListNode() for _ in range(size)]
        self.start_pointer = -1
        self.heap_start_pointer = 0

    def add_node_after(self, data, target_index):
        if self.heap_start_pointer < len(self.my_linked_list):
            new_index = self.heap_start_pointer
            self.heap_start_pointer += 1

            new_node = LinkedListNode(data)  # Set data for the new node

            if target_index == -1:
                # Insert at the beginning
                new_node.next_index = self.start_pointer
                self.start_pointer = new_index
            else:
                # Insert after the target node
                new_node.next_index = self.my_linked_list[target_index].next_index
                self.my_linked_list[target_index].next_index = new_index

            # Set data explicitly
            self.my_linked_list[new_index] = new_node

            return True
        else:
            print("Error: No more space in the heap.")
            return False

    def delete_node(self, target_index):
        if 0 <= target_index < len(self.my_linked_list):
            if target_index == self.start_pointer:
                # Deleting the first node
                self.start_pointer = self.my_linked_list[target_index].next_index
            else:
                # Deleting a non-first node
                prev_index = self.find_previous_index(target_index)
                if prev_index is not None:
                    self.my_linked_list[prev_index].next_index = self.my_linked_list[target_index].next_index

            # Reset the deleted node and move it to the heap
            self.my_linked_list[target_index] = LinkedListNode(next_index=self.heap_start_pointer)
            self.heap_start_pointer = target_index

            return True
        else:
            print("Error: Invalid target index.")
            return False

    def find_previous_index(self, target_index):
        current_index = self.start_pointer
        prev_index = None
        while current_index is not None and current_index != target_index:
            if current_index < 0 or current_index >= len(self.my_linked_list):
                break
            prev_index = current_index
            current_index = self.my_linked_list[current_index].next_index
        return prev_index

    def update_pointers(self):
        self.my_linked_list_pointers = []
        current_index = self.start_pointer
        while current_index is not None:
            self.my_linked_list_pointers.append(current_index)
            current_index = self.my_linked_list[current_index].next_index

    def print_linked_list(self):
        current_index = self.start_pointer
        while current_index is not None:
            new_node = self.my_linked_list[current_index]
            print(f"Index: {current_index}, Data: {new_node.data}, Next Index: {new_node.next_index}")
            current_index = new_node.next_index

# Example usage:
linked_list_size = 12
my_linked_list = LinkedList(linked_list_size)

# Add nodes
my_linked_list.add_node_after(42, -1)  # Add at the beginning
my_linked_list.add_node_after(13, 0)   # Add after the first node
my_linked_list.add_node_after(7, 1)    # Add after the second node

# Print the linked list
print("Linked List after adding nodes:")
my_linked_list.print_linked_list()

# Delete a node
my_linked_list.delete_node(1)

# Print the linked list after deletion
print("\nLinked List after deleting a node:")
my_linked_list.print_linked_list()

# Print pointers
print("\nPointers:")
my_linked_list.update_pointers()
print(my_linked_list.my_linked_list_pointers)
