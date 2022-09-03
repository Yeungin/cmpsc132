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
    contlst = contents.split()
    wordlst = []
    for ele in contlst:
        if ele.isalnum() is True:
            wordlst.append(ele)
        elif ele.isalnum() is False:
            for i in range (len(ele)):
                if ele[i].isalnum() is False:
                    if i != 0:
                        wordlst.append(ele[:i])
                    wordlst.append(ele[i])
                    if i != ((len(ele))-1):
                        wordlst.append(ele[i+1:])
    worddict = {}
    for i in range (len(wordlst)-1):
        worddict[wordlst[i]]=[]
    worddict['.'].append(wordlst[0])
    for i in range (len(wordlst)-1):
        worddict[wordlst[i]].append(wordlst[i+1])
    

    #worddict['.'].append(wordlst[1])

    return worddict

print(successors('items.txt'))