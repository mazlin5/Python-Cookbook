# First two elements are reserved for 0 and 1.. 
# each number is the sum of the preceding ones
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# iterative
def fib(n):
    # create starter arr sequence
    # seq = [0,1]
    # keep track of index
    start = 0
    next = 1
    empty = []

    # take [0,1] as input
    # determine a base case
        # until len(n) == 10
    if len(n) == 10:
        empty = [n]
    else:
        sum = n[start] + n[next]
        empty.append(sum)
            # increment indexes +=1
        start += 1
        next +=1
    return empty

    # use index add those two values as sum
    # append sum to array


# print(fib([0,1]))


# recursion
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def fib2(n):

    # ensure not neg and int
    assert n >= 0 and int(n) == n, 'Incorrect input type'

# use 0 and 1 as base case
    if n in [0,1]:
        return n
# recursive case should be f(n) = f(n-1) + f(n-2))
    return fib2(n-1) + fib2(n-2)

print(fib2(6))


