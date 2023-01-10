def factorial(n):
    # setup base case 
    assert n >= 0 and int(n) == n, 'Input types are incorrect'
    if n ==0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-3))

