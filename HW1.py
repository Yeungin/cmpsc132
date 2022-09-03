# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    lw = perimeter/2 #finding the sum of the length and width of the rectangle
    w = 0 #creating a variable for the side of the rectangle
    if lw.is_integer() is False: #checking if the sum is an integer or not
        return False

    for l in range (1,int(lw)): #loop through each possible pair of integers to find the other side of the rectangle
        w = lw - l
        if (w*l) == area:
            if w > l: #checking which side is larger
                return int(w)
            else:
                return int(l)


def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    #- YOUR CODE STARTS HERE
    inverse = {} #creating the inverse dictionary
    valuelst = [] #creating a list of dupicate values not allowed in inverse
    for keys in d: #iterating through the keys in d
        value = d[keys] #assigning the value at key in d to a variable
        if value in inverse: #checking if the value is already a key in the inverse
            inverse.pop(value) #removing the dupicate key
            valuelst.append(value) #adding to values not allowed as keys in inverse
        elif value not in valuelst: #checking if they key is allowed
            inverse.update({value:keys}) #creating the entry
    return inverse

def successors(file):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """

    with open(file) as f: 
        contents = f.read()

    #- YOUR CODE STARTS HERE
    contlst = contents.split() #split the file contents into words with punctuation attached
    wordlst = [] #create a list to contain elements from the file
    for ele in contlst:
        if ele.isalnum() is True: #check if the element is a word
            wordlst.append(ele)
        elif ele.isalnum() is False: #check if the element has punctuation
            for i in range (len(ele)):
                if ele[i].isalnum() is False: #add each possible part of the element (word, punctuation, word) to the list
                    if i != 0:
                        wordlst.append(ele[:i])
                    wordlst.append(ele[i])
                    if i != ((len(ele))-1):
                        wordlst.append(ele[i+1:])
                        
    worddict = {}
    for i in range (len(wordlst)-1): #create the keys in the dictionary with empty lists as values
        worddict[wordlst[i]]=[]
    worddict['.'].append(wordlst[0]) #add the first word as a value for '.'
    for i in range (len(wordlst)-1): 
        if wordlst[i+1] not in worddict[wordlst[i]]: #stops duplicates
            worddict[wordlst[i]].append(wordlst[i+1]) #fills the lists with words after the key

    return worddict
    
    

def getPosition(num, digit):
    """
        >>> getPosition(1495, 5)
        1
        >>> getPosition(1495, 1)
        4
        >>> getPosition(1495423, 4)
        3
        >>> getPosition(1495, 7)
        False
    """
    #- YOUR CODE STARTS HERE
    check = 0 # variable to keep the loop running
    count = 1 # variable to count which digit from the right we're on

    while check != 1:
        temp = num%10 #checking the current digit
        if temp == digit:
            check = 1
            return count
        elif temp < 1: #return false if the value becomes smaller than an integer
            check = 1
            return False
        else:
            num = num//10 #moving onto the next digit
            count += 1

def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    numlst = [num]  #creating a list starting with num
    while num != 1: #loop that ends when num reaches 1
        if (num%2) == 0: #if even 
            num = num/2
            numlst.append(int(num))
        elif (num%2) == 1: #if odd
            num = (3*num) + 1
            numlst.append(int(num))   
    return numlst

def largeFactor(num):
    """
        >>> largeFactor(15)
        5
        >>> largeFactor(80)
        40
        >>> largeFactor(13)
        1
    """
    #- YOUR CODE STARTS HERE
    check = 0 #to keep the loop running until it returns a value
    temp = num
    while check != 1:
        temp -= 1 #itterating through every integer less that num to find the largest factor
        if (num % temp) == 0:
            check = 1
            return temp




if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(rectangle, globals(), name='HW1',verbose=True) # replace rectangle for the function name you want to test
