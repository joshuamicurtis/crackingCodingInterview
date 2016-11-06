from linkList2 import *
from hashmap import HashTable

def palindrome(list1):
    if list1.head == None:
        return False
    list2 = HashTable(7)
    node = list1.head
    index = 0
    while node != None:
        list2[index] = node.data
        node = node.next_node
        index += 1
    count = 0
    node = list1.head
    
    while count != index:
        index -= 1 
        print "list1:", node.data
        print "list2", list2[index]
        if node.data != list2[index]:
            return False
        node = node.next_node
    return True
linkList1 = LinkedList()
linkList1.insertHead("R")
linkList1.insertHead("A")
linkList1.insertHead("C")
linkList1.insertHead("E")
linkList1.insertHead("C")
linkList1.insertHead("A")
linkList1.insertHead("R")
#linkList1.insertHead(1)
print palindrome(linkList1)