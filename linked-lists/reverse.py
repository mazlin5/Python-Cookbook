# Reverse a string 
# use recursive call for function 



# concat the first char to end of sliced string 

item = 'reverse'

def reverse(s):

    # start with base condition if len(string) == 0, return string
    if len(s) == 1:
        return s

    # else recursively call the reverse func to slice part of string except first char 
    return reverse(s[1:]) + s[0]

print(reverse(item))
