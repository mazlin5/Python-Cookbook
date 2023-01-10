# create global class to create Node 
# setting next => None means there is no link or end of list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# declare a class and constructor
class LinkedList:

        # constructor - create initial Node
        # method inside of class if using self 
        def __init__(self, value):
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1

        # to view all items in linked-list 
        # value:next = 'None' means you've reached end of list

        # create function of self and start at head
        def getList(self):
            temp = self.head

            # use while loop to traverse to end of list
            while temp is not None:
                print(temp.value)
                temp = temp.next

        #  create Node and add to end   
        def append(self, value):
            new_node = Node(value)

            # check if list is empty
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                # make first node refer to second node
                self.tail.next = new_node
                # add new node into list as tail 
                self.tail = new_node
                # increase length incrementally 
            self.length += 1

        def pop(self):
            temp = self.head
            pre = self.head

            if self.length == 0:
                return None
            else:
                # traverse through list where links are true
                while temp.next is not None:
                    pre = temp
                    # moves temp to next node
                    temp = temp.next
                self.tail = pre
                self.tail.next = None
                # decrement by 1
                self.length -= 1
            
            if self.length == 0:
                self.head = None
                self.tail = None
            # return node we just removed
            return temp.value

         # create Node add to head
        def prepend(self, value):
            # temp = self.head
            new_node = Node(value)

            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                # create link from self to self.head
                new_node.next = self.head
                # assing to head 
                self.head = new_node
            self.length += 1

        # remove first item in list
        def popFirst(self):
            temp = self.head

            if self.length == 0:
                return None
            else:
                # find first value and remove
                # moves temp to next node
                self.head = self.head.next
                # removes link - pops out node
                temp.next = None
                # decrement by 1
            self.length -= 1

            # if started with one item
            if self.length == 0:
                self.tail = None
            return temp.value

        # get item from linked list
        def get(self, index):
            # check to ensure index is valid
            if index == 0 or index >= self.length:
                return None
            else:
                temp = self.head
                # increment starting at the top since 
                for _ in range(index):
                    temp = temp.next
                return temp

        def set_value(self, index, value):
            # first get the value to change
            temp = self.get(index)

            # ensure boolean returns value
            if temp:
                temp.value = value
                return True
            return False

        # insert at specific index
        def insert(self, index, value):

            # first create new node 
            new_node = Node(value)

            if index == 0:
                # once run we end code in method
                return self.prepend(value)

            if index == self.length:
                return self.append(value)

            # point left of index you're pointing to
            temp = self.get(index - 1)
            # create link from new node to index value
            new_node.next = temp.next
            # add new node into list
            temp.next = new_node
            self.length += 1

        def remove(self, index):    
        # remove first item 
            if index == 0:
                return self.popFirst()
            # last item
            if index == self.length - 1:
                return self.pop()

            # arrow of item to left of item to remove
            # left item needs link to removed items old link
            # remove [2] from list of 4
            prev = self.get(index - 1)
            # since .get is O(n) use O(1)
            # temp = self.get(index)
            temp = prev.next
            # create link for left of removed item to item right of removed item
            prev.next = temp.next
            # remove item from list by terminating link
            temp.next = None
            self.length -= 1

        # MOST IMPORT LINKED LIST METHOD
        def reverse(self):
            temp = self.head
            # switch head and tail
            self.head = self.tail 
            self.tail = temp

            # var before and after temp
            # iterate through list with variables 
            after = temp.next
            # 
            before = None

            for _ in range(self.length):
                after = temp.next 
                temp.next = before
                before = temp
                temp = after

# init LinkedList constructor
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
# print(my_linked_list.get(3))
# my_linked_list.popFirst()
my_linked_list.set_value(1,8)
my_linked_list.getList()
# print(my_linked_list.pop())
# print(my_linked_list.pop())
# print(my_linked_list.pop())



    
