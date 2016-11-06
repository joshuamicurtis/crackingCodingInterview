from linkList2 import *

def partition(linkList1, part):
    if linkList1.head == None:
        return False
    less = LinkedList()
    more = LinkedList()
    node = linkList1.head
    while node != None:
        if node.data <= part:
            less.insertHead(node.data)
        else:
            more.insertHead(node.data)
        node = node.next_node
    node = less.head
    while node != None:
        if node.next_node == None:
            node.next_node = more.head
            break
        node = node.next_node
    return less

linkList1 = LinkedList()
linkList1.insertHead(10)
linkList1.insertHead(9)
linkList1.insertHead(1)
linkList1.insertHead(3)
linkList1.insertHead(8)
linkList1.insertHead(2)
linkList1.insertHead(4)
linkList1.insertHead(1)
linkList1.printList()
linkList1 = partition(linkList1, 5)
print "\n"
linkList1.printList()