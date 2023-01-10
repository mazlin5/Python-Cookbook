# if you have 2 sorted lists and its easy to combine into single list
# Ex. 8 unsorted items - break list in half then half again until each list have 1 item
# take two items and create a new sorted list until we have 4 lists 
#  do it again until 2 lists 
# combine all into one sorted list

# merge() - o(n)
#  merge takes 2 sorted list and combines them into new combined list
# loop through each list with i then j 
# compare i and j - lesser gets added to new combined list

def merge(list1, list2):
    # can't use for loops since (n) is unknown
    combined = [] 
    # index[0]
    i = 0
    j = 0

    # as long as both list still have items.. 
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            # move i over
            i += 1
        else:
            combined.append(list2[j])
            j +=1

    # pick up left overs
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined

# print(merge([1,2,7,8], [3,4,5,6]))


# breaks lists in half - make problem small  8 items = 3 steps o(n log(n))
# recursion until base-case: when len(list) = 1
# use merge() to put list back together 


def mergeSort(my_list):
    if len(my_list) == 1:
        return my_list

    # find midpont of list 
    # use int to turn 1.5 => 1 
    mid = int(len(my_list)/2)
    # give index of 2 up to mid
    left = my_list[:mid]
    # mid all the way to end of list
    right = my_list[mid:]

    return merge(mergeSort(left), mergeSort(right))

print(mergeSort([3,5,1,7,9,19, 11, 8, 20, 90]))
