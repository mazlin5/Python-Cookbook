# remove item off end of linked list 

# create class to create node
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None 

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.next = new_node
        self.length = 1
    
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
    
    # move to left - set tail.next = None and return value pop()
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
            return temp

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.getList()
# my_linked_list.pop()


                
        