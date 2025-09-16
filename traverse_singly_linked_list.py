

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse_and_print(head):
    current_node = head
    while current_node:
        print(current_node.data, end = " => ")
        current_node = current_node.next

    print("Null")


node1 = Node(11)
node2 = Node(3)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

traverse_and_print(node1)