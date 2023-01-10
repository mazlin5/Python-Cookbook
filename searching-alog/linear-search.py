# Want user to register - check if username exists in list or not 
# iterative through each element o(N) - o(1) space - unordered array

# unsorted array ONLY

# create func(arg1, arg2) - array, a value
# loop through array and check if current array[i] == value
# if True, return the index[i] at which element is found
# if array[i] is not found, return -1

def findValue(arr, val):

    # o(n)
    for i in range(len(arr)):
        if arr[i] == val:
            # o(1)
            return i  
    return -1

print(findValue([1,3,4,5,10,12], 51))


