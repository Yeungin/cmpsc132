# LAB3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given

def get_count(aList, item):
    '''
        >>> get_count([1,4,3.5,'1',3.5, 9, 1, 4, 2], 1)
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 3.5)  
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 9)   
        1
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 'a') 
        0
    '''
    ## YOUR CODE STARTS HERE
    
    if len(aList) == 0:  #if the list is empty return 0
        return 0
    else:
        if aList[-1] == item: #checking the rightmost element if it equals the item
            aList.pop(-1) #removing the rightmost element 
            return 1 + get_count(aList,item) #adding 1 to the returned integer
        else:
            aList.pop(-1) #removing the rightmost element
            return get_count(aList,item)


def replace(numList, old, new):
    '''
        >>> input_list = [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace(input_list, 1, 99.9)
        [99.9, 7, 5.6, 3, 2, 4, 99.9, 9]
        >>> input_list
        [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 5.6, 777) 
        [1, 7, 777, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 8, 99)    
        [1, 7, 5.6, 3, 2, 4, 1, 9]
    '''
    ## YOUR CODE STARTS HERE
    if len(numList) == 0: #checking if the list is empty
        return numList
    if numList[0] == old: #checking if the leftmost element is equal to old
        return [new] + replace(numList[1:], old, new) #creating a new list with the new element instead of the old
    else:
        curr = [numList[0]]
        return curr + replace(numList[1:], old, new) #if the element is not equal to old keep it the same in the returned list


def cut(aList):
    '''
        >>> cut([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> cut(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -3, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 0
        [5, 7, 6, 785, 5, 0, 42]
    '''
    ## YOUR CODE STARTS HERE
    if len(aList) == 0:
            return []
    if aList[0] < 0: #checking to see if the element is negative
        x = abs(aList[0])
        if len(aList) > 1:
            return cut(aList[x:])
        

    elif aList[0] >= 0:
        curr = [aList[0]]
        if len(aList) > 1: #if the element is positive return it, and move on to the next element
            return curr + cut(aList[1:])
        else:
            return curr


def neighbor(n):
    '''
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    '''
    ## YOUR CODE STARTS HERE
    x = n % 10 #check the rightmost
    y = n//10 #remove the rightmost
    if n == 0: #checking to see if the integer is 0
        return 0
    if x == (y%10): #checking rightmost vs 2nd rightmost
        return neighbor(y)
    elif y!=0: #if there are still more itterations needed
        return (neighbor(y))*10 + x #multiply the leftmost by 10, moving it over 1 space.
    else:
        return x #if y is equal to 0 this is the left most number

if __name__=='__main__':
    import doctest
    doctest.testmod()