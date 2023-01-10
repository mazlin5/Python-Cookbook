# Reverse string
# need a base case and recursive case

def reversal(n):

# start with base case to return last read element 
    if len(n) == 1:
        return n
    # since this starts at max -> first element[0] = len(n) == 1
    return reversal(n[1:]) + n[0]

print(reversal('some text backwards'))

