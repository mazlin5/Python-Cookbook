# Given an integer array, output all unique pairs that sum to a specific k
# input: [1,3,2,2], 4
# output: (1,3) (2,2)

# solution
# o(n) uses set data structure
# single scan of the array and for each element check where corresponding number 

def PairSum(s1, targetSum):
# declare temp counter
    # indx = 0

    if len(s1) <2:
        return 

    # create sets for tracking
    seen = set()
    output = set()

    # traverse 
    for item in s1:
        target = targetSum - item

        if target not in seen:
            seen.add(item)
        
        else:
            output.add( ((min(item,target)), max(item,target)) )
    return len(output)

print(PairSum([1,3,2,2], 4))
