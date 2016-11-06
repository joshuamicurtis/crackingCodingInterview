from linkList2 import *

def sum_list(list1, list2):
    if list1.head == None:
        return False
    if list2.head == None:
        return False
    total = 0
    place = 1
    node1 = list1.head
    node2 = list2.head
    while node1 != None or node2 != None:
        if node1 != None:
            total += node1.data * place
            node1 = node1.next_node
        if node2 != None:
            total += node2.data * place
            node2 = node2.next_node
        place = place * 10
    print "Total:", total
    listStr = str(total)
    finalList = LinkedList()
    for char in listStr:
        finalList.insertHead(int(char))
    return finalList
linkList1 = LinkedList()
linkList1.insertHead(9)
linkList1.insertHead(1)
linkList1.insertHead(3)
linkList1.insertHead(2)
linkList1.printList()
linkList2 = LinkedList()
linkList2.insertHead(5)
linkList2.insertHead(4)
linkList2.insertHead(3)
linkList2.printList()
finalList = sum_list(linkList1, linkList2)
finalList.printList()

