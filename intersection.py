from linkList2 import *

x = 0
y = x
print id(x)
print id(y)
x = 1
print id(x)
print id(y)

linkList1 = LinkedList()
linkList1.insertTail(9)
linkList1.insertTail(1)
linkList1.insertTail(3)
linkList1.insertTail(2)
print "List1:"
linkList1.printList()
linkList2 = LinkedList()
linkList2.insertTail(5)
linkList2.insertTail(4)
linkList2.insertTail(linkList1.head.next_node.data)
linkList2.insertTail(5)
linkList2.insertTail(4)
print "List2:"
linkList2.printList()