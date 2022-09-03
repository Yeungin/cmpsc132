# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement



class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(4.5)
        >>> x.add(-3)
        >>> x.add(0)
        >>> x.add(5)
        >>> x.add(2)
        >>> x.add(-9)
        >>> x.add(12.7)
        >>> x.add(-3.5)
        >>> x.add(2)
        >>> x.add(4)
        >>> x.add(1)
        >>> x.add(3)
        >>> x
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -3.5 -> -3 -> 0 -> 1 -> 2 -> 2 -> 3 -> 4 -> 4.5 -> 5 -> 12.7
        >>> x.replicate()
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -9 -> -3.5 -> -3.5 -> -3 -> -3 -> 0 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4.5 -> 4.5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 12.7 -> 12.7
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -3.5 -> -3 -> 0 -> 1 -> 2 -> 3 -> 4 -> 4.5 -> 5 -> 12.7
        >>> x.add(0)
        >>> x.add(3)
        >>> x
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -3.5 -> -3 -> 0 -> 0 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4.5 -> 5 -> 12.7
        >>> myList=x.replicate()
        >>> myList
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -9 -> -3.5 -> -3.5 -> -3 -> -3 -> 0 -> 0 -> 1 -> 2 -> 2 -> 3 -> 3 -> 3 -> 3 -> 3 -> 3 -> 4 -> 4 -> 4 -> 4 -> 4.5 -> 4.5 -> 5 -> 5 -> 5 -> 5 -> 5 -> 12.7 -> 12.7
        >>> myList.removeDuplicates()
        >>> myList
        Head:Node(-9)
        Tail:Node(12.7)
        List:-9 -> -3.5 -> -3 -> 0 -> 1 -> 2 -> 3 -> 4 -> 4.5 -> 5 -> 12.7
        >>> x.add(13)
        >>> x.add(13)
        >>> x
        Head:Node(-9)
        Tail:Node(13)
        List:-9 -> -3.5 -> -3 -> 0 -> 0 -> 1 -> 2 -> 3 -> 3 -> 4 -> 4.5 -> 5 -> 12.7 -> 13 -> 13
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-9)
        Tail:Node(13)
        List:-9 -> -3.5 -> -3 -> 0 -> 1 -> 2 -> 3 -> 4 -> 4.5 -> 5 -> 12.7 -> 13
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        new_node = Node(value) #create a node with the given value
        current = self.head 
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            while current:
                if new_node.value <= current.value:# if the new node is the lowest value
                    new_node.next = current
                    self.head = new_node
                    break
                elif current.next == None: #if the new node is greater than every value in the linked list
                    current.next = new_node
                    self.tail = new_node
                    break    
                elif new_node.value > current.value and new_node.value <= current.next.value: #to place a node at the beginning or somewhere in the linked list
                    new_node.next = current.next
                    current.next = new_node
                    break
                
                current = current.next



    def replicate(self):
        # --- YOUR CODE STARTS HERE
        rep = SortedLinkedList() #creating a new linkedlist 
        current = self.head
        while current:
            if current.value == 0: #condition if value = 0
                rep.add(0)
            elif current.value < 0 or isinstance(current.value, float): # if value is a float or negative you add it once after the original add
                rep.add(current.value)
                rep.add(current.value)
            elif current.value > 0: #if the value is a positive integer it is added to the list as many times as its value.
                for i in range (current.value):
                    rep.add(current.value)
            current = current.next
        if rep.isEmpty(): #return nothin if the list is empty
            return None
        return rep


    def removeDuplicates(self):
        # --- YOUR CODE STARTS HERE
        current = self.head
        while current:
            if current.next == None: #end the loop if on the last node
                break
            elif current.value == current.next.value: #check if the current node is equal to the next
                temp = current.next                   #removing the duplicate nodes from the list by linking the current node to the .next of the next and then delinking the next
                current.next = temp.next
                temp = None
            else:                                     #this is here to continuously check the same value, this is the case if there are multiple duplicates of the same value.
                current = current.next
        