class MinStack(object):
    def __init__(self):
        self.container = []
        self.min = None
        
    def push(self, data):
        if self.min == None or data < self.min:
            self.min = data
        self.container.append(data)
    
    def min_pop(self):
        if len(self.container) == 0:
            return False
        elif len(self.container) == 1:
            item = self.container[-1]
            del self.container[-1]
            self.min = None
            return item
        elif len(self.container) > 1:   
            item = self.container[-1]
            del self.container[-1]
            if item == self.min and self.min not in self.container:
                newMin = self.container[0]
                for i in self.container:
                    if i < newMin:
                        newMin = i
                self.min = newMin
            return item
    
    def peek(self):
        return self.container[-1]
    
    def get_min(self):
        return self.min
        
st = MinStack() 
st.push(2)
st.push(3)
st.push(1)
st.push(1)
print "peek", st.peek()
print "min", st.get_min()
print "pop", st.min_pop()
print "min", st.get_min()
print st.container
print "pop", st.min_pop()
print "min", st.get_min()
print "peek", st.peek()
print st.container