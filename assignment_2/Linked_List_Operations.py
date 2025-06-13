class Node:
    def __init__(self, data):
        self.data = data    
        self.next = None      

class LinkedList:
    def __init__(self):
        self.head = None      

    # Add a node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:      # If list is empty, make new_node the head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:  # Move to the end of the list
                current = current.next
            current.next = new_node          # Add new_node at the end
    def print_list(self):
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # End of the list

    # Delete the nth node (1-based index)
    def delete_nth_node(self, n):
        if self.head is None:
            print("Error: List is empty. Nothing to delete.")
            return

        if n <= 0:
            print("Error: Index must be 1 or more.")
            return

        # If deleting the first node
        if n == 1:
            print(f"Deleting node at position 1 with data: {self.head.data}")
            self.head = self.head.next
            return

        # Traverse to the node before the one to delete
        current = self.head
        count = 1
        while current is not None and count < n - 1:
            current = current.next
            count += 1

        # If next node is None, index is out of range
        if current is None or current.next is None:
            print("Error: Index out of range.")
            return

        print(f"Deleting node at position {n} with data: {current.next.data}")
        current.next = current.next.next  # Skip the deleted node

# ----------- Testing the LinkedList ------------
if __name__ == "__main__":
    # Create a new LinkedList object
    my_list = LinkedList()

    # Add some items to the list
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    print("Original List:")
    my_list.print_list()

    # Delete the 2nd node
    my_list.delete_nth_node(2)

    print("List after deleting 2nd node:")
    my_list.print_list()

    # Try deleting an invalid index
    my_list.delete_nth_node(10)

    # Try deleting from an empty list
    empty_list = LinkedList()
    empty_list.delete_nth_node(1)
