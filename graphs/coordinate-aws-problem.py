# sets - unordered collection of items, that don't allow duplicates. order does not matter
# backed with hash table lookup - o(1) 

directions = ['N', 'S', 'E', 'W']
coordinates = {'N': (-1,0),
               'S': (1,0),
               'E': (0,-1),
               'W': (0,1)
               }

# set starting place
i, j = 0, 0

visited = set.add((i,j))

for direction in directions:
    # iterate through an store visition first coordinate
    i = i + coordinates[direction][0]
    j = j + coordinates[direction][1]
    # check if visited
    if (i,j) in visited:
        True
    visited.add((i, j))
False



# An Amazon employee is walking around a fulfillment center and picking up items for customers.  
# We want to know if they have to backtrack a lot as they do this, because there may be a more 
# efficient set of items we could give them to pick.

# Given a list of cardinal directions (north, south, east, west) that represents their steps, 
# determine if they re-crossed their path as they walked around.*


#time complexity requirement? space complexity requirement?

## Examples
# [ N, E, S, W, W ] -> True
# [ ]N, S] -> True
# [ ] -> False
# [ N, N, E, E, E ] -> False
# [ N, E, E, E, S, W ] -> False

## Solutions
# Represent the points as coordinates and store the visited coordinates
# List is size N.  Add N coordinates to the set.  Adding to the set is O(1) so overall O(N).
# Space complexity is O(N) in the worst case, where the path never crosses.

# [N, N, E, S, W] (0,1) - remove N

# directions = ['N', 'E', 'S', 'W', 'W']
# coordinate = {
#     'N': (0, 1),
#     'S': (0, -1),
#     'W': (-1, 0),
#     'E': (1, 0)
# }
# i, j = 0, 0

# visited = set()
# visited.add((i, j))

# pos = (0, 0)
# for direction in directions:
#     i = i + coordinate[direction][0]
#     j = j + coordinate[direction][1]
#     if (i, j) in visited:
#         True
#     visited.add((i, j))
# False

