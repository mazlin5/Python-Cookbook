# to view all items in linked-list 
# value:next = 'None' means you've reached end of list

# create function of self and start at head
def getList(self):
    temp = self.head

    # use while loop to traverse to end of list
    while temp is not None:
        print(self.value)
        temp = temp.next




