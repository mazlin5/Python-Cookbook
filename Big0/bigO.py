# O(n) n = # of operations to run
# linear/proportional as n -> infinitity

def print_items(n):
    # for loop that runs N times
    for i in range(n):
        print(i)
    
    # ran 2n times -> O(n)
    # drop constnats
    for j in range(n):
        print(j)

print_items(10)
