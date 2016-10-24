from hashmap import HashTable
from linkList2 import *
from random import randint

def delete_dups(linkList):
    # Deletes duplicates in a linked list
    #linkList.printList()
    H = HashTable(7)
    pointer = linkList.head
    #linkList.delete(3)
    #print pointer.next_node.data
    while pointer != None:
        #print pointer.data
        if pointer.data in H.data:
            linkList.delete(pointer.data)
        else:
            H[randint(1,100)] = pointer.data
        pointer = pointer.next_node    
    print H.data
    linkList.printList()
linkList = LinkedList()
linkList.insertHead(1)
linkList.insertHead(1)
linkList.insertHead(2)
linkList.insertHead(1)
linkList.insertHead(2)
linkList.insertHead(3)
delete_dups(linkList)