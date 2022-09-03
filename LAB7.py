# LAB7
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

class MinBinaryHeap:
    '''
        >>> h = MinBinaryHeap()
        >>> h.insert(10)
        >>> h.insert(5)
        >>> h
        [5, 10]
        >>> h.insert(14)
        >>> h._heap
        [5, 10, 14]
        >>> h.insert(9)
        >>> h
        [5, 9, 14, 10]
        >>> h.insert(2)
        >>> h
        [2, 5, 14, 10, 9]
        >>> h.insert(11)
        >>> h
        [2, 5, 11, 10, 9, 14]
        >>> h.insert(14)
        >>> h
        [2, 5, 11, 10, 9, 14, 14]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20]
        >>> h.insert(20)
        >>> h
        [2, 5, 11, 10, 9, 14, 14, 20, 20]
        >>> h.getMin
        2
        >>> h._leftChild(1)
        5
        >>> h._rightChild(1)
        11
        >>> h._parent(1)
        >>> h._parent(6)
        11
        >>> h._leftChild(6)
        >>> h._rightChild(9)
        >>> h.deleteMin()
        2
        >>> h._heap
        [5, 9, 11, 10, 20, 14, 14, 20]
        >>> h.deleteMin()
        5
        >>> h
        [9, 10, 11, 20, 20, 14, 14]
        >>> len(h)
        7
        >>> h.getMin
        9
    '''

    def __init__(self):   # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self._heap=[]
        
    def __str__(self):
        return f'{self._heap}'

    __repr__=__str__

    def __len__(self):
        return len(self._heap)

    @property
    def getMin(self):
        # YOUR CODE STARTS HERE
        return self._heap[0]                #the top of the heap is the min num
    
    
    def _parent(self,index):
        # YOUR CODE STARTS HERE
        if index <= 1:                      #access the index of the parent and return the value
            return None
        parent_index = index//2
        return self._heap[parent_index-1]

    def _leftChild(self,index):
        # YOUR CODE STARTS HERE             #access the index of the leftchild and return the value
        if index < 1:
            return None
        left_index = (index*2)-1
        if left_index > len(self._heap)-1:
            return None
        return self._heap[left_index]

    def _rightChild(self,index):
        # YOUR CODE STARTS HERE             #access the index of the rightchild and return the value
        if index < 1:
            return None
        right_index = index*2
        if right_index > len(self._heap)-1:
            return None
        return self._heap[right_index]


    def insert(self,item):
        # YOUR CODE STARTS HERE
        self._heap.append(item)
        index = len(self._heap)
        check = 0
        while check == 0:                   
            parent = self._parent(index)        #check if the item is smaller than the parent, if so percolate up via swap
            if parent is None:
                return None
            elif item >= parent:
                return None
            else:
                self._heap[index-1] = parent
                self._heap[(index//2)-1] = item
                index = index//2
        

    def deleteMin(self):
        # Remove from an empty heap or a heap of size 1
        if len(self)==0:
            return None        
        elif len(self)==1:
            deleted=self._heap[0]
            self._heap=[]
            return deleted
        else:
            # YOUR CODE STARTS HERE
            min = self._heap[0]
            self._heap[0] = self._heap.pop(len(self._heap)-1)   #remove and replace the root with the rightmost leaf
            index = 1
            check = 0
            while check == 0:
                left_child = self._leftChild(index)                     
                right_child = self._rightChild(index)
                if left_child is None and right_child is None:      #check if the node is a leaf
                    return min
                elif left_child is not None and right_child is None:    #since the tree is complete, the only other combination of none is left and none childs, in which only compare left and parent
                    if self._heap[index - 1] > left_child:
                        self._heap[(2*index)-1] = self._heap[index-1]
                        self._heap[index-1] = left_child
                        index = 2*index
                        return min
                    else:
                        return min
                elif self._heap[index - 1] < left_child and self._heap[index - 1] < right_child:    #if the node is less than the children its done
                    return min
                elif self._heap[index - 1] > left_child and self._heap[index - 1] > right_child:    #if the node is greater than both children swap with the smaller child
                    if right_child < left_child:
                        #swap parent and right child
                        self._heap[2*index] = self._heap[index-1]
                        self._heap[index-1] = right_child
                        index = (2*index)+1
                    else:
                        #swap parent and left child
                        self._heap[(2*index)-1] = self._heap[index-1]
                        self._heap[index-1] = left_child
                        index = 2*index
                elif self._heap[index - 1] > left_child:            #else compare left to swap
                    self._heap[(2*index)-1] = self._heap[index-1]
                    self._heap[index-1] = left_child
                    index = 2*index
                elif self._heap[index - 1] > right_child:           #else compare right to swap
                    self._heap[2*index] = self._heap[index-1]
                    self._heap[index-1] = right_child
                    index = (2*index)+1
                
                


def heapSort(numList):
    '''
       >>> heapSort([9,1,7,4,1,2,4,8,7,0,-1,0])
       [-1, 0, 0, 1, 1, 2, 4, 4, 7, 7, 8, 9]
       >>> heapSort([-15, 1, 0, -15, -15, 8 , 4, 3.1, 2, 5])
       [-15, -15, -15, 0, 1, 2, 3.1, 4, 5, 8]
    '''
    # YOUR CODE STARTS HERE
    heap = MinBinaryHeap()
    lst = []
    for ele in numList:     #add each element in the list to the heap
        heap.insert(ele)
    size = len(heap._heap)
    for i in range (size):  #remove each min and add it to the list, which sorts it from least to greatest
        temp = heap.deleteMin()
        lst.append(temp)
    return lst

