class ThreeInOne(object):
    
    def __init__(self, stack_size):
        self.arr = []
        for i in range(stack_size * 3):
            self.arr.append(None)
        self.index1, self.start1 = 0, 0
        self.index2, self.start2 = len(self.arr)/3, len(self.arr)/3
        self.index3, self.start3 = len(self.arr)*2/3, len(self.arr)*2/3
        print len(self.arr)*2/3
        
    def insertArr(self, index, startPos, nextStartPos, data):
        print "index: %s  nextstartpos: %s" % (index, nextStartPos)
        if index == nextStartPos:
            for i in range(index - startPos):
                self.arr.insert(index, None)
            self.arr[index] = data
            return index - startPos
        self.arr[index] = data
        return 0 
    
    def push(self, stack, data):
        if stack == 1:
            insertValue = self.insertArr(self.index1, self.start1, self.start2, data)
            self.index1 += 1
            if insertValue < 0:
                self.start2 += insertValue
                self.start3 += insertValue
        if stack == 2:
            insertValue = self.insertArr(self.index2, self.start2, self.start3, data)
            self.index2 += 1
            if insertValue < 0:
                self.start3 += insertValue
        if stack == 3:
            self.insertArr(self.index3, self.start3, len(self.arr), data)
            self.index3 += 1 

    def pop(self, stack):
        if stack == 1:
            if self.index1 <= selt.start1:
                return False
            item = self.arr[self.index1 - 1]
            self.arr[self.index1 - 1] = None
            self.index1 -= 1 
            return item
        if stack == 2:   
            if self.index2 <= selt.start2:
                return False
            item = self.arr[self.index2 -1]
            self.arr[self.index2 - 1] = None
            self.index2 -= 1 
            return item
        if stack == 3:    
            if self.index3 <= selt.start3:
                return False
            item = self.arr[self.index3 - 1]
            self.arr[self.index3 - 1] = None
            self.index3 -= 1 
            return item
            
    def peek(self, stack):
        if stack == 1:
            print "index1", self.index1 -1
            return self.arr[self.index1 - 1]
        if stack == 2:
            print "index2", self.index2 -1
            return self.arr[self.index2 - 1]
        if stack == 3:
            print "index3", self.index3 -1
            return self.arr[self.index3 - 1]
            
threeStacks = ThreeInOne(2)
print threeStacks
threeStacks.push(1, 10)
threeStacks.push(2, 20)
threeStacks.push(3, 30)
print threeStacks.peek(1)
print threeStacks.peek(2)
print threeStacks.peek(3)
print threeStacks.pop(1)
print threeStacks.pop(2)
print threeStacks.pop(3)
print threeStacks.peek(1)
print threeStacks.peek(2)
print threeStacks.peek(3)
threeStacks.push(1, 10)
threeStacks.push(2, 20)
threeStacks.push(3, 30)
threeStacks.push(1, 11)
threeStacks.push(2, 21)
threeStacks.push(3, 31)
threeStacks.push(1, 12)
threeStacks.push(2, 22)
threeStacks.push(3, 32)
print threeStacks.peek(1)
print threeStacks.peek(2)
print threeStacks.peek(3)