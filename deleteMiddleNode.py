from linkList2 import *

def delete_mid_node(node):
    if node == None or node.next_node == None:
        return False
    node.data = node.next_node.data
    node.next_node = node.next_node.next_node
    return True

linkList1 = LinkedList()
linkList1.insertHead("Begin")
linkList1.insertHead("at")
linkList1.insertHead("Head")
linkList1.printList()
delete_mid_node(linkList1.head.next_node)
linkList1.printList()