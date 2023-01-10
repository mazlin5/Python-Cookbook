def fizzBuzz(n):
    # Write your code here
    for i in range(1,n+1):
        output = ''
        if (i%3==0) and (i%5==0):
            output+= 'FizzBuzz'
        if (i%3==0) and not(i%5==0):
            output+='Fizz'
        if (i%5 == 0) and not(i%3==0):
            output+='Buzz'
            # not divisible
        if output == '':
            output+= str(i)
        print(output)  

fizzBuzz(100)
