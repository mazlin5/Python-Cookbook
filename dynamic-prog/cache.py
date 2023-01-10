# return  a sum 

# not dynamic you have to run x times
def getSum(n):
    print('long time')
    return n + 80

# global scope so you don't overrite hash table
cache = {}
# dynamic cache approach
def getSum2(n):
    if (n in cache):
        return cache[n]
    else:
        print('not in cache please wait..')
        cache[n] = n + 80
    return cache[n]

print(getSum2(5))
print(getSum2(6))
print(getSum2(5))
print(cache)
