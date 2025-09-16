

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


def delete_node(head, node_to_delete):
    # check if the element you want to delete is the head or not
    if head == node_to_delete:
        # if it is the head, so the head will be the next node, because the head
        # will be delete
        return head.next
    
    current_node = head # initialize the current_node to be the value of head
    # to use it to check on the other links

    while current_node.next and current_node.next != node_to_delete: # while current_node not empty
        # if the next node and next next node are not equal to the node_to_delete
        # to check if the node_to_delete exist or not
        current_node = current_node.next

    if current_node is None: # if it runs until the end and doesn't find node_to_delete
        # then the node_to_delete not here. So we can return the old list again with
        # the old head
        return head
    
    current_node.next = current_node.next.next # this is the most important one
    # because, we are at the link before the one we need to delete. So
    # we need to skip the one we need to delete, and put the pointer or link
    # to the next one from the node_to_delete point

    return head # we returning the head if it changed or not, to complete
    # the calculations if needed.