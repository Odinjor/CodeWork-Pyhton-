
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    #Creates the head for the last person to point back to making it circular
    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def remove(self, node):
        current = self.head
        if current == node:
            self.head = self.head.next
        else:
            while current.next != self.head:
                if current.next == node:
                    current.next = node.next
                    break
                current = current.next

def potato(n, k):
    # Create the circular linked list
    linked_list = LinkedList()
    for i in range(n):
        linked_list.append(i)

    current = linked_list.head
    while current.next != current:
        # Iterate k-1 times to find the node to remove
        for _ in range(k - 1):
            current = current.next
        # Remove the node
        linked_list.remove(current)
        current = current.next  # Move to the next person after removal

    return linked_list.head.data

# Example usage:
n = 11  # Number of people in the group
k = 8   # Number of steps in one iteration of the rhyme
print(potato(n, k))  # Output: 8
             
