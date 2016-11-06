#from stack import Stack

class Set_Of_Stacks(object):
    def __init__(self):
        self.stack_list = []
        self.current_stack = 0
        self.stack_list.append(None)
        self.stack_list[self.current_stack] = []
        
    def push(self, data):
        print "length current_stack", len(self.stack_list[self.current_stack])
        if len(self.stack_list[self.current_stack]) >= 10:
            self.current_stack += 1
            print "self.current_stack", self.current_stack
            try: self.stack_list[self.current_stack]
            except IndexError:
                self.stack_list.append(None)
                self.stack_list[self.current_stack] = []
        self.stack_list[self.current_stack].append(data)
    
    def pop(self):
        if len(self.stack_list[self.current_stack]) == 0:
            self.current_stack -= 1
        try:
            return self.stack_list[self.current_stack].pop()
        except IndexError:
            return None
    
    def peek(self):
        return self.stack_list[self.current_stack][-1]
        
    def pop_at(self, idx):
        return self.stack_list[idx].pop()
        
sos = Set_Of_Stacks()
print sos.pop()
print sos.stack_list
sos.push(1)
sos.push(2)
sos.push(3)
sos.push(4)
sos.push(5)
sos.push(6)
sos.push(7)
sos.push(8)
sos.push(9)
sos.push(10)
sos.push(11)
sos.push(12)
print sos.stack_list
print sos.pop()
print sos.stack_list
print sos.pop()
print sos.stack_list
sos.push(13)
sos.push(14)
print sos.stack_list
