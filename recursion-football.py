
# 315 - American Football Score
# In a simplified game of American football, teams score points by either achieving a touchdown (7 points) or a field goal (3 points).

# Given the score for a single team, please return how many different permutations of touchdowns and/or field goals exist in order to arrive at that score.

# Input: Integer
# Output: Integer
# Examples
# Input:  10
# Output: 2

# Explanation: For a score of 10, the output would be 2. The 2 ways to arrive at
# this score is to:

# 1) Score a field goal (3 points) and then touchdown (7 points)
# 2) Score a touchdown (7 points) and then field goal (3 points)


# Input: 21
# Output: 2

# Explanation: For a score of 21, the output would be 2. The 2 ways to arrive at
# this score is to:

# 1) Score 7 field goals (3 * 7 points)
# 2) Score 3 touchdowns (7 * 3 points)


# Input:  16
# Output: 4

# Explanation: For a score of 16, the output would be 4. The 4 ways to arrive at
# this score is to:

# 1) Score 1 touchdown (7 points) and 3 field goals (3 * 3 points)
# 2) Score 1 field goal (3 points), then 1 touchdown (7 points), and then 2 field goals (2 * 3 points)
# 3) Score 2 field goals (2 * 3 points), then 1 touchdown (7 points), and lastly 1 field goal (3 points)
# 4) Score 3 field goals (3 * 3 points) and then 1 touchdown (7 points)

# input [7, 3] - total = x
# output the number paths to total (int)

#                 0,0 - input
#               3     7
#            3   7   3   7
#         
#                               16, [0,0]
#  sub last item and return                  .pop() last item and return 
#                                     0
#                        3                             7
#                   6      10                  10             14  
#              9     13     13  17(T)    13   17(T)         17(T)   21(T)
#           12  16  16 (T) 16 (T)       16 (T)           
#         15 (T)     
     # t   t 
# two choices use or use 3

# 2 field goals -> 1 touch  -> 1 field goal 

def findWays(num):
  # init
  print("jhello")
  count = 0
  def helper(runningNum):
    if runningNum > num:
      return 
    if runningNum == num:
      count + 1
      return count 

    # left 
    helper(runningNum + 3)
    helper(runningNum + 7)

    helper(num)

  return count

# print(findWays(16))


# print("hello")