# Problem 1
# Find sum of digits of a position integer
# for 3 digit int, divide by 10 one extra time
# digit = 123, then return 6


def findSum(n):

    # fault tolerent 
    assert n >= 0 and int(n) == n, 'Incorrect input'
    # base case 
    if n == 0:
        return 0
    else:
        return int(n%10) + findSum(int(n/10))

# print(findSum(123))


# Problem 2
# How to recursively take power of a number

def powR(base, exp):

    # use rule that power of 0 = 1
    if exp == 0:
        return 1
    else:
        print(base, "exp:",exp)
        return base * powR(base,exp - 1)
# print(powR(10,2))


# Problem 3
# How to find greatest commond divisor of two integers

# find the max(num) thats divisible to two nums
def gcd(num, num2):

    if num2 == 0:
        return num
    else:
        print(num2)
        return gcd(num2, num%num2)

print(gcd(8,12)) 

# step 1 divide both numerbs and get reult 
# divide second value by remainder above
# divided remainder above by second remainder

# gcd(a, 0) =A
# gcd(a,b) = gcd(b, a, MOD(b)
