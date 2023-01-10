# lookup o(n)  :  pop,push, peek o(1)
# LIFO - need to know very last value that was added
# Examples------ 
# browser history, re-do function - store previous state in memory so recent comes first

# [1,2,3,4] => first out.. pop() 

class Stack():  #o(1)
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.items = []

# check if empty

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.items) == self.maxSize:
            return True
        else:
            return False

# push a new item
    def push(self, value):
        if (self.isFull):
            self.items.append(value)
            return True
        else:
            return False

# pop an item 
    def get(self):
        if not (self.isEmpty):
            return 'No elements in stack'
        else:
            self.items.pop()

# peek at top of item
    def peek(self):
        if self.items:
            return self.items.pop()
        
# return size
    def getSize(self):
        if not (self.isEmpty):
            return len(self.items)
        False

customStack = Stack(4)
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack.isFull())
print(customStack.items)
customStack.get()
print(customStack.items)
print('last elm: ', customStack.peek())


