# replacing an array with larger array since o(n) 
# use algorithm amortization to optimize append operation
# allocate memoory for larger array of size
# copy old to new array and feed to new array

# find matching letters of strings
# declare vars to track index position for each array 
# traverse single array
# if array1[0] == array2[0] then array2 indx +=1
# now +=1 array1 until you reach end of array len()

def anagram(arr1, arr2):

    # clean up strings and lowercase everything
    arr1 = arr1.replace(' ', '').lower()
    arr2 = arr2.replace(' ', '').lower()

    print(arr1, arr2)
    # edge case check if same num of letters
    if len(arr1) != len(arr2):
        return False
    
    # create counting dict
    count = {}

    for letter in arr1:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] = 1

    for letter in arr2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False
    return True

anagram('God', 'doGn')
