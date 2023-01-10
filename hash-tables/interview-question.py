# Given two list determine if each has item in common

arr1 = [1, 3, 16, 7]
arr2 = [2, 4, 9, 10, 11, 22, 16]

# o(n^2) brute force solution 
def findComp(arr1, arr2):
    # create a starting index for each 
    # index0 = 0

    common = []
# for loop that take [0] of first array and iterate through second
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                common.append(arr1[i])
                j += 1
    # return item from list that were both agree
    return common

print(findComp(arr1, arr2))


# more efficient solution using dict and hash tables

# loop through first and insert into ht o(n)
# 
# {
#     1: True,
#     3: True,
#     16: True,
#     7: True
# }

# loop through 2nd list thats o(n)
def findComp2(arr1, arr2):
    # empty empty dictonary
    empty_dict = {}

    # loop first list
    for i in arr1:
        empty_dict[i] = True
    
    # seperate loop 
    for j in arr2:
        if j in empty_dict:
            return j

    return False

print(findComp2(arr1, arr2))