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


def delete_node(head, node_to_delete):
    if head == node_to_delete:
        return head.next
    
    current_node = head

    while current_node.next and current_node.next != node_to_delete:
        current_node = current_node.next
    
    if current_node.next is None:
        return head
    
    current_node.next = current_node.next.next

    return head


def insert_node(head, new_node, pos):
    if pos == 1:
        new_node.next = head
        return new_node
    
    current_node = head

    for _ in range(pos - 2):
        if current_node is None:
            break
        current_node = current_node.next

    new_node.next = current_node.next
    current_node.next = new_node
    
    return head


    