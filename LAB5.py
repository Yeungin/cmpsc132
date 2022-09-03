# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x.insert(11)
        >>> x.insert(2)
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> x.getMin
        Node(2)
        >>> x.getMax
        Node(11)
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.isEmpty()
        False
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
        >>> new_tree = x.mirror()
        11 : 10 : 9.5 : 9 : 7 : 5 : 4 : 2 : 
        >>> new_tree.root.right
        Node(4)
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)         


    def mirror(self):
        # Creates a new BST that is a mirror of self: 
        #    Elements greater than the root are on the left side, and smaller values on the right side
        # Do NOT modify any given code
        if self.root is None:
            return None
        else:
            newTree = BinarySearchTree()
            newTree.root = self._mirrorHelper(self.root)
            newTree.printInorder
            return newTree
        




    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.root == None: #if the root is None the tree is empty
            return True
        return False



    def _mirrorHelper(self, node):
        # YOUR CODE STARTS HERE
        if isinstance(node, Node) == False:
            return None
        newNode = Node(node.value) #creating a new node for the new tree
        newNode.right = self._mirrorHelper(node.left) #setting the child of the new to the opposite child of the old
        newNode.left = self._mirrorHelper(node.right) 
        return newNode
        
    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        node = self.root
        while node.left is not None: #because the tree is sorted, keep on moving left to get the smallest node
            node = node.left
        return node


    @property
    def getMax(self): 
        # YOUR CODE STARTS HERE
        node = self.root
        while node.right is not None: #because the tree is sorted, keep on moving right to get the largest node
            node = node.right
        return node

    def __contains__(self,value):
        # YOUR CODE STARTS HERE
        if self.isEmpty == True: #return none if the tree is empty
            return None
        node = self.root
        while node is not None:    #because we can assume the node is in the tree, navigate it until you find the node
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            elif value == node.value:
                return True
        return False



    def getHeight(self, node):
        # YOUR CODE STARTS HERE
        if self.isEmpty == True:
            return None
        value = node.value
        node = self.root
        while node.value != value:   #navigate the tree until you reach the desired node
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
        return self._getHeightHelper(node)
    
    def _getHeightHelper(self,node): 
        if node:
            return 1 + max(self._getHeightHelper(node.left),self._getHeightHelper(node.right)) #find the maximum depth via recursion on both sides of the tree
        else:
            return -1 #remove 1 because this 'none' is not a node
        



