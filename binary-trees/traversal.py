# In a BST, an inorder successor of a node is 
# the node with the smallest value > than the value
# of input node..

# Given a node inputNode in a BST, you're asked to 
# write a function that returns the inorder successor of inputNode
# if inputNode has no inorder successor return null


# BST - Traversal: Depth first search 
# Differ in order which nodes are visited

# Pre order - root -> left -> right
def preorder(tree):

    # base case - check if tree exists
    if tree:
        print(tree.getRootVal())
        preorder(tree.getleft())
        preorder(tree.getRight())

# another example o(n)
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.getRootVal())
    preorder(rootNode.left)
    preorder(rootNode.right)


# In order - left -> root -> right
def inorder(rootNode):

    # base case - check if tree exists
    if rootNode != None:
        return
    inorder(rootNode.getleft())
    print(rootNode.getRootVal())
    inorder(rootNode.getRight())
        

# Post order - left -> right -> root 
# move call to print to end of function

def postorder(tree):

    # base case - check if tree exists
    if tree != None:
        postorder(tree.getleft())
        postorder(tree.getRight())
        print(tree.getRootVal())


def findClosestValueInBst(tree, target):

    # base case 
    if (tree):
        #  recursive case to check if inputNode.right is empty
        if inputNode.right != None:
            return getLeftMost(inputNode.right)
        # if inputnode.right is empty climb tree to find next highest val
        node parent = child.parent
        node child = child

        # going up the tree 
        while parent.right == child:
            if parent.parent is None:
                return null
            child = parent
            parent = parent.parent
        return parent
    
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

