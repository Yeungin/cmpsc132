# HW4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# You might add additional methods to encapsulate and simplify the operations, but they must be
# thoroughly documented


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
        >>> x.insert('mom')  
        >>> x.insert('omm') 
        >>> x.insert('mmo') 
        >>> x.root          
        Node({'mmo': ['mom', 'omm', 'mmo']})
        >>> x.insert('sat')
        >>> x.insert('kind')
        >>> x.insert('ats') 
        >>> x.root.left
        Node({'ast': ['sat', 'ats']})
        >>> x.root.right is None
        True
        >>> x.root.left.right
        Node({'dikn': ['kind']})
    '''

    def __init__(self):
        self.root = None


    # Modify the insert and _insert methods to allow the operations given in the PDF
    # Document all the modifications done
    def insert(self, value):
        sort = ''.join(sorted(value))  #create the key for the dictionary
        dic = {sort:[value]}           #create the dict to assign as a value
        if self.root is None:
            self.root=Node(dic)        #assign dict instead of value
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        sort = ''.join(sorted(value))           #find the sorted word
        dic = {sort:[value]}                    #create a dict to be the node's value
        key = list(node.value.keys())[0]        #access the key of the node's value
        if sort == key:                         #if the sorted and key are the same, add the word to the list in the node
            node.value[sort].append(value)
            return None
        if(sort<key):                           #compare the ascii values of the sorted with the key
            if(node.left==None):
                node.left = Node(dic)           #create a new node with the dict as the value
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(dic)          #create a new node with the dict as the value
            else:
                self._insert(node.right, value)


    def isEmpty(self):
        return self.root == None

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

class Anagrams:
    '''
        # Verify class has _bst attribute  
        >>> x = Anagrams(5)
        >>> '_bst' in x.__dict__    
        True
        >>> isinstance(x.__dict__.get('_bst'), BinarySearchTree)
        True
        >>> x = Anagrams(5)
        >>> x.create('words_small.txt')
        >>> x.getAnagrams('tap')
        'No match'
        >>> x.getAnagrams('arm')
        'No match'
        >>> x.getAnagrams('rat')
        ['art', 'tar', 'rat']
        >>> x._bst.printInorder
        {'a': ['a']} : {'adns': ['ands', 'sand']} : {'ahms': ['sham', 'hams']} : {'amt': ['tam', 'mat']} : {'arst': ['arts', 'rats', 'star']} : {'arsty': ['artsy']} : {'art': ['art', 'tar', 'rat']} : 
    '''
    
    def __init__(self, word_size):
        # -YOUR CODE STARTS HERE        #create the bst and an object with the max size
        self._bst = BinarySearchTree()
        self.maxsize = word_size


    def create(self, file_name):
        # -YOUR CODE STARTS HERE
        # Code for reading the contents of file_name is given in the PDF
        with open(file_name) as f:      #open the file
            content = f.readlines()

        for i in content:               #iterate through each line in the file
            word = i.strip()            #if the line is blank or is larger than the max size go to the next line, otherwise insert the word into the tree
            if len(word) == 0:
                continue
            if len(word) > self.maxsize:
                continue
            else:
                self._bst.insert(word)


    def getAnagrams(self, word):
        # -YOUR CODE STARTS HERE
        sort = ''.join(sorted(word))                #organize the letters of the word and navigate the tree to find the combination                
        ans = self._navigate(self._bst.root, sort)  #if its in the tree return the words, otherwise return no match
        if ans is None:
            return "No match"
        else:
            return ans

    def _navigate(self, node, sort):        #helper method for getAnagrams
        key = list(node.value.keys())[0]    #recursively go through the bst, checking if sort is the same as the node, if not, go left if its less or right if its greater.
        if sort == key:                     #return none if its not in the tree.
            return node.value[key]
        elif sort < key:
            if node.left is None:
                return None
            return self._navigate(node.left, sort)
        elif sort > key:
            if node.right is None:
                return None
            return self._navigate(node.right, sort)



