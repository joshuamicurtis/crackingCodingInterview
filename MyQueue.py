class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.tempstack = []
        
    def add(self, data):
        self.stack1.append(data)
        
    def peek(self):
        while len(self.stack1) > 0:
            self.tempstack.append(self.stack1.pop())
        data = self.tempstack.pop()
        self.tempstack.append(data)
        self.tempstack.reverse()
        self.stack1 = self.tempstack
        self.tempstack = []
        return data
        
    def remove(self):
        while len(self.stack1) > 0:
            self.tempstack.append(self.stack1.pop())
        data = self.tempstack.pop()
        self.tempstack.reverse()
        self.stack1 = self.tempstack
        self.tempstack = []
        return data
        
mq = MyQueue()
mq.add(1)
mq.add(2)
mq.add(3)
mq.add(4)
print mq.peek()
print mq.remove()
print mq.stack1
print mq.peek()
print mq.remove()
print mq.stack1