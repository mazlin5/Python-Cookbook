# FIFO data structure - pop(0) '
# Examples - waitlist app, resy, uber, print
# lookup - o(n) enqueue/dequeue/peek o(1)   - peek = who is the first person 

# list = o(n)
# linked list = 

import queue 

q = queue.Queue()
for val in range (5):
    q.put(val)
print(q)
# check qsize
# customQue.put(1)
# customQue.put(2)
# customQue.put(3)
# print(customQue.maxsize)

    