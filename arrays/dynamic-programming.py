/**
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:
#        1
#      1   1
#    1   2   1
#   1  3   3   1 
# 1   4  6   4   1
#

# Input: numRows = 1
# Output: [[1]]
# input: numRows = 2
# Output: [[1],[1,1]]

# input = n
# output = [[n]]

#  take the initial input
#  return it, +1 
#  look at first,second indices -> add
#  return the first index & sum with the second value 





#
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

#                 0  1  2  3
# # input nums = [2, 3, 7, 5]
# # output = 10

#tabulation - create an array of same shape of input and insert answers in there 
# identify clear recusrive realtiopn to slowly fill out table - order depends on relationship (look abck 1 and 2 elements)

#  0 1 2  3 4
# [2 7 9  3  1]

# [2 7 11 11 12]
#  0 1 2 3 4 5 


# Time: O(N)

# Space: O(N)