# Lab #1
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

def isValid(txt):
    '''
        >>> isValid('qwertyuiopASDFGHJKLzxcvbnm')
        True
        >>> isValid('hello there, fall is here!')
        False
        >>> isValid('123456yh')
        False
        >>> isValid('POIUYTqwerASDFGHlkjZXCVBMn')
        True
        >>> isValid('POIUYTqwerASDFGHlkjZXCVBnn')
        False
        >>> isValid('12aaaaaaaaaaa6543212345678')
        False
    '''
    # - YOUR CODE STARTS HERE -
    pass





def get_words(filename):
    '''
        Complete the current implementation to work as directed in the handout. No more than 3 lines are required

        .txt file for this doctest is available on Canvas and must be saved in the same directory as your .py file
        >>> get_words('contents.txt')
        ['week', 'bat', 'aquatic', 'eggs', 'threatening', 'crash', 'educated', 'adjoining', 'bent', 'mice', 'belief', 'adjustment', 'blood', 'smooth', 'kaput', 'mountain', 'digestion', 'enchanted', 'wandering', 'fresh']
        >>> len(get_words('contents.txt'))
        20
    '''
    output = []
    with open(filename) as text: # Open, read and close file
        for line in text:        # text contains the entire content of the .txt file
            # - YOUR CODE STARTS HERE -
            pass






def get_histogram(words):
    '''
        >>> get_histogram(['hello', 'there', 'spring', 'is', 'here'])
        {5: 2, 6: 1, 2: 1, 4: 1}
        >>> list_of_words = get_words('contents.txt')
        >>> get_histogram(list_of_words)
        {4: 4, 3: 1, 7: 1, 11: 1, 5: 4, 8: 2, 9: 4, 6: 2, 10: 1}
    '''
    # - YOUR CODE STARTS HERE -
    pass




def removePunctuation(aString):
    '''
        >>> removePunctuation("Dots...................... many dots..X")
        ('Dots                       many dots  X', {'.': 24})
        >>> data = removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
        >>> data[0]
        'I like chocolate cake      It s the best flavor      for real'
        >>> data[1]
        {'!': 4, '(': 1, "'": 1, '.': 3, ';': 1, '$': 1}
        
    '''
    # - YOUR CODE STARTS HERE -
    pass





if __name__ == "__main__":
    import doctest
    #doctest.run_docstring_examples(get_words, globals(), name='LAB1',verbose=True)   ## Uncomment this line if you want to run doctest by function. Replace get_words with the name of the function you want to run
    #doctest.testmod() ## Uncomment this line if you want to run the docstring in all functions
