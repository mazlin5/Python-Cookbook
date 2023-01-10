# Given a string list all possible permutions of string
# example string = 'abc' return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# cannot repeat values 
# want to append occurence mixture in list 

# return the string 
# swap the +1 element with last element 
# increment to +1 and return first og element to the end 
# continue.. until len == 1

def permute(n):

     # create empty list to store permutations
    output = []

# reducing the len of list by 1 at each recursion 
    if len(n) == 1:
        output = [n[:]]
    else:
        # iterate through inital string 
        # for each char, set aside that char and get list of all permutations of the string thats left
        for i, let in enumerate(n):            
    # if cur iteration is 'b' - want all permutions remaining 'ac'
            for perm in permute( n[:i] + n[i+1:]):
                # list2 = [let,perm]
                # add to output
                output 
            
  
    return output

print(permute([1, 2, 3]))


