

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_lowest_value(head):
    min_value = head.data
    current_node = head.next

    while current_node:
        if current_node.data < min_value:

            min_value = current_node.data
        
        current_node = current_node.next

    return min_value

node1 = Node(11)
node2 = Node(3)
node3 = Node(5)
node4 = Node(9)
node5 = Node(2)
node6 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(f"Lowest value in singly linked list is: {find_lowest_value(node1)}")
