# First In First Out 
# cannot insert into middle - only head or end
#  onkly remove from the beginning 
# Call center - you side in queue until next available agent finishes a call (currently)

# operations - create, enqueu, dequeue, peek, isEmpty, isFull, deleteQueue

# createQueue = [] - insertion = enqeue, 
# customeQueue.enqueue(2) - o(n) ts when queue is full - (err) isFull
# customQueue.deqeue(1) - .pop() end -> end -1 -> end - 2... [4,3,2]
class Queue:
    def __init__(self):
        self.items = []

# peek method - customeQueue = [1,2,3,4] .peak -> 1
# just want to check first element 
 
# customeQueue = [1,2,3,4] returns False 

# isFull() - if capacity is reached you cannot insert anymore 
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
# deleteQueue()

# isEmpty() - external function 0(1)
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            values = [i for i in self.items]
            print('These items are present: ',values)

    # insert element to queue - AT THE END o(n)
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at end of list"

    # o(n) time complexity - since you have to shift items
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "This queue is empty"
        else:
            return self.items[0]

    def delete(self):
        self.items = None

m = Queue()   
m.enqueue(1)
m.enqueue(2)
m.enqueue(3)
m.enqueue(4)
m.enqueue(5)
# print(m.dequeue())
print(m.dequeue())
