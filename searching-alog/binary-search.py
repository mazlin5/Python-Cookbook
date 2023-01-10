# works only with sorted array 
# half of remainging elements can be ignored

# start in middle and check left or right if inputVal is < or >
# divide and conquer using MERGE SORT

# create function with 2 params which are sorted array and value
# create pointers for left and right nodes
# based on left and right calc middle pointer
# while middle is not == value and start <= end loop

# Big O - o(log n)

def binarySearch(arr, value):
    start = 0
    end = len(arr) - 1
    middle = int(start+end//2)
   

    while not(arr[middle]==value):
        if value < arr[middle]:
            # move init end point to val -1 than len
            end = middle -1
        else:
            start = middle + 1

        # every time we need to update middle value
        middle = int((start+end)//2)
        # print(start, middle, end)

    # edge case if searching val == middle element
    if arr[middle] == value:
        return middle
    else:
        return -1

custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 20))

