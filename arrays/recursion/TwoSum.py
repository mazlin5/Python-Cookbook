# recursion traversion and array 
# functions that call themselves within their definitions 

# brute force solution is to double nest a loop over the list where 
# the inner loops only looks at index greater than what the outer loop
# is currently on 

# get input array
def twoNumberSum(array, targetSum):
    # sum = 0
    # drop non-dominants
    for i in array:
        for j in array:
            if (i + j == targetSum):
                return (i, j)

# get input array
def twoNumberSum2(array, targetSum):
    storage = set(array)
    
    # drop non-dominants
    for i in array:
        target = targetSum - i
        if target in storage and target is not i:
            return [target, i]
    return []

print(twoNumberSum2([1, 15, 18, 9, 5], 10))
 

 