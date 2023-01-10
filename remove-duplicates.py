# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    temp = linkedList
    while temp is not None:
        nextNode = temp.next
        while nextNode is not None and nextNode.value == nextNode.value:
            nextNode = nextNode.next
        temp.next = nextNode
        temp = nextNode
    return linkedList