# don't specify how large the array is beforehand
# list instance has greater capacity than current len(array)

# key is to provide means to grow array A that store elements of list
# cant' actually grow the array its capacity is fixed..
# if element if appended to list at a time when the array is full.. perform the following..

# allocate a new array B with larger capacity
#  set b[i] = a[i] for i = 0 .. n-1 where n = number of items
#  set a = b 
# insert new elements in b


# import sys

# def testArr():
#     n = 50
#     data = []

#     for i in range(n):
#         # number of elements
#         a = len(data)
        
#         # actual size of bytes
#         b = sys.getsizeof(data)

#         print(a, b)
#         # print(data)

#         data.append(n)

#     # print(data)

# testArr()

# import cytpes for storage array 
import ctypes
import sys

class DynamicArray(object):

    # create array
    def __init__(self) -> None:
        
        # length of array
        self.n = 0
        # accept one element by default
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n
    
    # get item or return element at index
    def __getitem__(self, k):

        # use index to return element at index
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds')

        # if above clears return val at index
        return self.A[k]

    # add element at end of array
    def append(self, value):

        # check capacity
        if self.n == self.capacity:
            # if too small resize and double
            self._resize(2*self.capacity) 

        self.A[self.n] = value
        self.n +=1
        
    def _resize(self, new_cap):
        B = self.make_array(new_cap)

        # reference all existing from a - b
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        return (new_cap * ctypes.py_object)()
    
    def checkSize(self):
# number of elements
     return sys.getsizeof(self.A)
        
    
arr = DynamicArray()
arr.append(1)
arr.checkSize
arr.append(2)
arr.checkSize
arr.append(3)
arr.append(4)
arr.checkSize
# print(arr[2])  
# class M(object):

#     def public(self):
#         print("Use tab to see me")

#     def _private(self):
#         print("You won't be able to tab to see me")

# m = M()