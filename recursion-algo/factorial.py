# 4! = 4 * 3 * 2 * 1
# if n=0 then n! = 1 - "base case occurs when n = 0"

# Always think of the base case as you will need to return the 
# base case once all recursion cases have been worked through

# function calls itself recursively
def factorial(n):
    # consider base for when reach end of recursion
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# 2! = 2 * 1
print(factorial(5))

