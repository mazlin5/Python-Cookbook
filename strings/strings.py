# strings are stored as ADCII in bits in memeory 
#  o(1) operations 
# traverse string - o(n) operation - o(1) space
# copy - o(n) st
# get - o(1) st - string is stored as array of integers
# insert - makes a copy with new char at the end - there is no set at index (immutable string)

# o(n^2) t where n is len(string) because each addition of a char to newString creates an entirely new string 
#  and is itself an o(n) operation. n o(n) operations performed => o(n^2) t overall 

# mutable obj = list, dict, set (changeable)
# immutable obj = int, float, string, tuple, bool

# python handles args to function based on mutable or immutable 
# if mutable obj if called by reference, original var may be changed. 

def increment(n):
    n += 1
b = 9
# when pass b an arg, local var n refer to the same obj
# however int are immutable so create new obj w/ value 10 and assign to n
# var n is pointing to diff obj from what b is pointing to
# now n refers to an obj w/ value 10 but b still refers to obj with value 9
print(increment(b)) 
print(b)

# string = "this is a string2"
# newString = []

# for character in string:
#     for rec in len(string):
#         newString.append(character[rec])
#         rec += 1

# print(newString)




