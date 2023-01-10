
# 231 - Capital Permutations
# Given a string str of lowercase alphabetical characters, return the set of all permutations of those characters in upper AND lowercase.

# Advanced
# Solve the same problem, except now you may have number characters in your string (which don't have a lowercase or uppercase, but should still be included in your result) and capital letters, that need to be lowercased.

# Input: str (String)
# Output: [Str] (Array of Strings)
# Example
# Input: "abc"
# Output: ["ABC", "ABc", "AbC", "aBC", "Abc", "aBc", "abC", "abc"]

# input = 

"aab"
# 'aab'
# output = ['aab', 'aba', '']

#          i
# string = abc

# add some empty list  - 
# ab   
#  i               ""
#               a                A
#           ab   aB          Ab       AB
#        abc abC aBc aBC   Abc AbC  ABc ABC

       # left call 
#       callerFunc(lower(currVal[i]) + lower(currVal[i+ 1]))
#     
#     right call 
 #     callerFunc(upper(currVal[i]) + upper(currVal[i]+1))
# 
#     help func
#     callerFunc('',0)
#      
#     return 
#  left=lower
#  right= uper
# 
# ab .Ab, aB, AB
#  i
# 

# def findCombos(string):
#   result = []
#   def callerFunc(running_s, indx):
#     if len(running_s) == len(string):
#        result.append(running_s)
#        return 
#     # recursion       ""
#     # left side 
#     callerFunc(running_s+string[indx], indx + 1)
#     # right side     
#     callerFunc(running_s + string[indx].upper(), indx + 1)
    
#   callerFunc("",0)
  
#   return result

# string = 'abcd'

# print(findCombos(string))



# Advanced:

# Input: "A1d3"
# Output: ["A1D3", "a1D3", "A1d3", "a1d3"]

def findSet(string):
  result = []

  # runningS and index
  def helper(runningS, index):
    # base case is when len of created string = len(input)
    if (len(runningS) == len(string)):
      result.append(runningS)
      return 

    # ignore numbers
    # left side 

    helper(runningS + string[index].lower(), index+1)
      # right side 1
    if not (string[index].isnumeric()):
      helper(runningS + string[index].upper(), index +1)
  # start
  helper('', 0)
  
  return result
# print result
string = 'A1d3'

print(findSet(string))

