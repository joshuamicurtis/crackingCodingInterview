def sort_stack(stack1):
    temp_stack = []
    temp = None
    print stack1
    while len(stack1) > 0:
        temp = stack1.pop()
        while len(temp_stack) > 0 and temp_stack[-1] > temp:
            stack1.append(temp_stack.pop())
        temp_stack.append(temp)
    return temp_stack
       
stack1 = []
stack1.append(6)
stack1.append(4)
stack1.append(2)
stack1.append(3)
stack1.append(1)
stack1.append(5)
stack1.append(0)
stack1 = sort_stack(stack1)
print  stack1