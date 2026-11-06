class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data , end=" -> ")
            current_node = current_node.next
    def pop(self):
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

linked_list = LinkedList()
linked_list.append("apple")
linked_list.append("banana")
linked_list.append("orange")
linked_list.append("grape")
linked_list.display()
print(linked_list.pop())

