from linkList2 import *

def klast(linkList, k):
    if linkList.head == None:
        return False
    pointer = linkList.head
    count = 0
    while pointer != None:
        count += 1
        pointer = pointer.next_node
    
    if k >= count:
        return False
    target = count - k 
    pointer = linkList.head
    i = 0
    while i < target:
        pointer = pointer.next_node
        i += 1
    return pointer.data
k = 3
linkList = LinkedList()
linkList.insertHead(1)
linkList.insertHead(2)
linkList.insertHead(3)
linkList.insertHead(4)
linkList.insertHead(5)
linkList.insertHead(6)
linkList.printList()
print "%d element is %d" % (k, klast(linkList, k))