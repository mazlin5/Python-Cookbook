# Design a system that manages the reservation state of n seats that are number from 1 to n.
# Implement the SeatManager class:

# SeatManager(int n) Init a SeatManager object that will manage n seats numbered from 1 to n..
# {'1': '[0]',
#  '2': '[1]',     [1,2,4,5,6]
#  '3': '[1]',
#  '4': '[1]',
# } 
# *All seats are initially available SeatManager(4) = 4 seats 
# set some available property to false 

# int reserver() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number
# get [0] of array where not in reserved 

# Questions 
# do we know how many seats are there beforehand

# binary search using heap - brute force solution 

class SeatManager(object):
    def __init__(self, n):
            self.avaiable = 0
            self.seats = [None] * n 
            # [1,2,3,4]
    
    # Fetches the smallest-numbered unreserved seat, reserves it, and returns its number
    def reserve(self):
        reserved = []
        # assuming ordered list get smallest item
        unreserve = self.seats.pop(0) 
        self.avaiable = 1

        if unreserve:
            # reserve it!
            reserved.append(unreserve)
            self.avaiable = 0
        
     # void unreserve(int seatNumber) Unreserves the seat with the given seatNumber 
    # .pop() last element in the reserved list and return to queue (insertion logic?)
    # edge cases => does it exists or isNot None:, or is seatNumber in range of available seats   
    def unreserve(self, seatNumber):

        if seatNumber in self.seats:
            self.seats.append(unreserve)
        return unreserve

