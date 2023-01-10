# Given two arrays of int, write function that determines whether the 
# second array is a subsequence of first one

# same order [1, 3, 4] is subsequence of [1, 2, 3, 4]

# hint
# interate through main array and look for [0] in the subsequence 
# if true: keep iterating through the main array but now look for [1]
# continue until you find every int in subseq or reach the end of main array

# declare var holding position in subseq
# at first this be [0] in subseq as you find values in main array
# you'll increment the position variable until you reach the end

# o(n) to search entire array by length n
# not storing anything that += in size

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def isValidSubsequence(array, sequence):
    # initialize index at [0]
    indx = 0
    for num in range(len(array)):
        if array[num] == sequence[indx]:
            indx += 1
        if indx == len(sequence):
            return True
    return False

isValidSubsequence([1, 4, -1, 7], [4, 7, 5]) 

# traverse both in tandem to keep track of positions for both arrays 
arridx = 0
seqidx = 0
while arridx < len(array) and seqidx < len(sequence):
    # seeking to match current element in sequence and subarray
    if array[arridx] == sequence[seqidx]:
        seqidx += 1
        # keep moving along main array
    arridx += 1
    # return when reach end of sequence
return seqidx == len(sequence)