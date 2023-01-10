 # edge case when you need to get left minVal
    def getLeftMost(x):
        while (x.left is not None):
            return x
        return getLeftMost(x.left)
    
    # if you have to go up
    # check if tree exists
    # check node.right == current_node
    # if upperNode > currentNode.left: return 
    
    # if you have to go down
    # check node.right exits:
    # check if node.left exists:
    # continue down node.left until empty

# remove node in BST
 # if node to delete has 1 child 
        # relink child.left/righth to child.parent

        # if node to delete has 2 child or root node
        # successor = minVal in right subtree 

# if you want to remove root you need to replae with minVal of right subtree (in order succcesor)
#
def getLeftMost(node):
    while node.left != None:
        return node
    return getLeftMost(node.left)

# check root node
def deleteNode(rootNode, inputNode):
    if rootNode is None:
        # then we have no element to delete
        return rootNode

    if inputNode < rootNode:
        rootNode.left = deleteNode(rootNode.left, inputNode)
    elif inputNode > rootNode:
            rootNode.right = deleteNode(rootNode.right, inputNode)
    
    else:
        if rootNode.left is None:
            temp = rootNode.left
            rootNode = None
            return temp

        if rootNode.right is None:
            temp = rootNode.right
            rootNode = None
            return temp
        
        # node has two children
        # find minVal succesor 
        temp = getLeftMost(rootNode.right)
        rootNode.value = temp.value
        # delete minVal of right subtree
        rootNode.right = deleteNode(rootNode.right, temp.value)

    return rootNode