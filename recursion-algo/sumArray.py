# Given an array of numbers return the sum 

# ensure list is ordered, if not sort it

def sum(n):
    if n ==1:
        return 1
    return n + sum(n-1)

# print(sum(4))


# Given an int, create function that returns sum of all indiviudal elements
# example: n = 4321 return 4+3+2+1

def sumString(n):
    for i, v in enumerate(n):
        if i == 1:
            return 1
        return v + sumString()

# print(sumString(4321))



     
     
