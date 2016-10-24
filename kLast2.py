from linkList2 import *

def klast(linkList, k):
    if linkList.head == None:
        return False
    pointer1 = linkList.head
    pointer2 = linkList.head
    count = 0
    while count < k:
        if pointer1 == None:
            return False
        count += 1
        pointer1 = pointer1.next_node
    
    while pointer1 != None:
        pointer1 = pointer1.next_node
        pointer2 = pointer2.next_node
    return pointer2.data
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