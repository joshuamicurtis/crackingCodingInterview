from linkList2 import *
from stack import *

def palindrome(linkList):
    fastNode = linkList.head
    slowNode = linkList.head
    
    stack = Stack()
    
    while fastNode != None and fastNode.next_node != None:
        stack.push(slowNode.data)
        slowNode = slowNode.next_node
        fastNode = fastNode.next_node.next_node
    
    # There are an odd number of elements, so middle element must be skipped
    if fastNode != None:
        slowNode =slowNode.next_node
    
    while slowNode != None:
        top = stack.pop()
        print top
        if top != slowNode.data:
            return False
        slowNode = slowNode.next_node
    
    return True
linkList1 = LinkedList()
linkList1.insertHead("R")
linkList1.insertHead("A")
linkList1.insertHead("C")
linkList1.insertHead("E")
linkList1.insertHead("C")
linkList1.insertHead("A")
linkList1.insertHead("T")
#linkList1.insertHead(1)
print palindrome(linkList1)
        
        
    
    