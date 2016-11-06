class Stack(object):
    def __init__(self):
        self.container = []
    
    def push(self, item):
        self.container.append(item)
    
    def pop(self):
        try:
            return self.container.pop()
        except:
            print "Error: nothing in stack to pop"
    
    def peek():
        try:
            return self.containter[-1]
        except:
            print "Error: nothing in stack to peek"
    
    def is_empty(self):
        return (self.container == [])