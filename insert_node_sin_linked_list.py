
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverse_and_print(head):
    current_node = head
    while current_node:
        print(current_node.data, end = " -> ")
        current_node = current_node.next

    print("Null")


def insert_node(head, new_node, pos):
    if pos == 1: # check if the position is the head or not
        new_node.next = head # if the position is the position, so move the old head
        # to be the second element of the linked list, and the new_node will be 
        # placed in the first position
        return new_node # return new_node instead of the head
    
    current_node = head # define the current_node to be the head to continue

    for _ in range(pos - 2): # this to get the position after and before
        if current_node is None: # check if is not found or what
            break # if not found, then break the loop
        current_node = current_node.next # make the current_node to be the next one

    new_node.next = current_node.next # make the new_node the next also, so here 
    # we link the previous to the new
    current_node.next = new_node # and here we link the next to the new
    return head # then return the head to work anyways

node1 = Node(11)
node2 = Node(5)
node3 = Node(8)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

print("Before:")
traverse_and_print(node1)

new_node = Node(97)

node1 = insert_node(node1, new_node, 3)

print("After:")
traverse_and_print(node1)