# start off with our list representation 

class BinaryHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # insertion - append() 
    # compare newly added node with its parent 
    # # if newly added is < parent then we can swamp the item with its parent
    def percUp(self,i):
        while i // 2 > 0:
            # heaplist at that index - 
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    