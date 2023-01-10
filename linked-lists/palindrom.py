# Given the head node of a singly linked list, return true if the values of the linked list forms a palindrome.

# 13577531

#  (1) -> (2) -> (3) -> (3) -> (2) -> (1)
#         ^
#         |
# Input: (1)
# Output: True

#        (1) -> (2) -> (4) -> (2) -> (1)
#         ^
#         |
# Input: (1)
# Output: True

#        (5) -> (8) -> (4) -> (1) -> (7)
#         ^
#         |
# Input: (5)
# Output: False

# store this in a array
# start at head node
# check if headNode exists..
# loop while headNode is not None
# append nodes into array
# headNode = node.next

# new pointer = 0
# end point = len(result) - 1

#  0         5
# while point < end point
# compare result[new pointer] vs result[end pointer]
# if not the same ..
# false

# increment pointers
# return true


class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class llList:

  def __init__(self, value):
    newNode = Node(value)
    self.head = newNode
    self.tail = newNode
    self.length = 1

  def append(self, value):
    # edge case to check if empty
    newNode = Node(value)
    if self.length == 0:
      self.head = newNode
      self.tail = newNode
    else:
      #
      self.tail.next = newNode
      self.tail = newNode
    self.length += 1

  def getList(self):
    temp = self.head

    # while
    while temp is not None:
      print(temp.value)
      temp = temp.next

# store this in a array
# start at head node
# check if headNode exists..
# loop while headNode is not None
# append nodes into array
# headNode = node.next

# new pointer = 0
# end point = len(result) - 1

#  0         5

  def isPalindrome(self, head):
    # store output
    result = []
    head = self.head

    while head is not None:
      result.append(head.value)
      head = head.next

    left = 0
    right = len(result) - 1

    # while point < end point
    # compare result[new pointer] vs result[end pointer]
    # if not the same ..
    # false
    while (left < right):
      if result[left] != result[right]:
        return False

      #
      left += 1
      right -= 1
    return True

# increment pointers
# return true

m = llList(5)
m.append(5)
m.append(2)
m.append(2)
m.append(5)
m.append(6)
print(m.getList())
print(m.isPalindrome(5))

# i
# 22223456765438
#              j