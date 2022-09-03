# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
        self.items = [] #a list to hold the nodes in the stack
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        # YOUR CODE STARTS HERE 
        return self.items == [] #returns True if the stack is empty

    def __len__(self): 
        # YOUR CODE STARTS HERE
        return len(self.items) #output the amount of nodes on the stack

    def push(self,value):
        # YOUR CODE STARTS HERE
        newNode = Node(value)      #create a new node to push onto the stack
        newNode.next = self.top    #make the node under the new node the current top
        self.items.append(newNode) #adding the new node to the stack
        self.top = newNode         #making the new node the top node
     
    def pop(self):
        # YOUR CODE STARTS HERE
        if len(self.items) != 0:   #making sure there are nodes to remove
            temp = self.top        #saving the current top node
            self.items.pop()       #removing the top node
            self.top = temp.next   #making the top node the node after the previous node
            return temp.value      #returning the value of the node removed

    def peek(self):
        # YOUR CODE STARTS HERE
        return self.items[len(self.items)-1].value #returning the value of the node on top of the stack


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            float(txt)   #check if txt is is a number
            return True
        except:
            return False




    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary


        '''
        
        postfixStack = Stack() #order stack
        dic = {'^': 4,'*': 3, '/': 3, '+': 2, '-': 2, '(': 1} #dict of mathematical symbols and their priority
        diccheck = {'^': 4,'*': 3, '/': 3, '+': 2, '-': 2,}
        lst = [] #output list
        txtLst = txt.split()
        past = None
        ele = len(txtLst)
        parcheck = 0

        if txt == None or txt == '': #if there is no txt return none
            return None 

        for i in range (ele):
            #check for invalid conditions
            if self._isNumber(txtLst[i]) == True and self._isNumber(past) == True: #if 2 numbers are one after another
                return None
            elif txtLst[i] in diccheck and past in diccheck: #if there are 2 operators next to eachother
                return None
            elif txtLst[i] in dic and i == ele-1: #if the final character is an operator
                return None
            elif txtLst[i] == "(" and self._isNumber(past) == True: #check for implied multiplication
                return None
            elif self._isNumber(txtLst[i]) == True and past == ")":
                return None
            elif txtLst[i] == "(" and past == ")":
                return None
            elif txtLst[i] == "(": #count if there are an even amount of open and closed brackets
                parcheck += 1
            elif txtLst[i] == ")":
                if parcheck < 1:
                    return None
                parcheck -= 1
            past = txtLst[i]
        
        if parcheck != 0: #invalid if wrong number of parenthesis
            return None
            
        for element in txtLst:
            if self._isNumber(element) == True: #check if the element is a number
                lst.append(str(float(element))) 
            elif element == '(':                #check if the element is an open bracket
                postfixStack.push(element)
            elif element == ')':                #check if the element is a closed bracket
                top = postfixStack.pop()        #checking the top node and removing it from the stack
                while top != '(':               #run until the '(' is removed
                    lst.append(top)             #add the top to the end of the list
                    top = postfixStack.pop()
            else:
                if element in dic:              #if the element is a mathematical symbol
                    while (not postfixStack.isEmpty()) and (dic[postfixStack.peek()] >= dic[element]):     #while there are nodes on the stack and the next top has higher priority add the top to the lst
                        if element == "^" and postfixStack.peek() == "^":
                            break
                        lst.append(postfixStack.pop())
                    postfixStack.push(element) #otherwise, add another element to the top of the stack
                else:
                    return None #invalid if special character
        while (not postfixStack.isEmpty()): #adding the stack to the list
            lst.append(postfixStack.pop())
        
        return ' '.join(lst) #returning the postfix


    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( ( ( 10 - 2 * 3 ) ) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('( 3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5 ) - 15 + 85 ( 12 )') 
            >>> x.calculate
            >>> x.setExpr("( -2 / 6 ) + ( 5 ( ( 9.4 ) ) )") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression
        

        # YOUR CODE STARTS HERE
        postFix = self._getPostfix(self.__expr) #getting the postFix expression 
        if postFix == None:   #if there is no postFix expression or the expression is invalid return nothing 
            return None

        lst = postFix.split() #split the postFix expression into a list

        for element in lst: #itterate through each element in the list
            if self._isNumber(element) == True: #if the element is a number add it to the stack
                calcStack.push(float(element))
            else:   #if the element is an operator
                num2 = calcStack.pop() 
                num1 = calcStack.pop()
                if element == "*": #multiply
                    num3 = num1 * num2
                elif element == "/": #divide
                    num3 = num1 / num2
                elif element == "+": #add
                    num3 = num1 + num2
                elif element == "-": #subtract
                    num3 = num1 - num2
                elif element == "^": #power
                    num3 = num1**num2
                calcStack.push(num3) #add the resulting number from the operation to the stack
        return calcStack.pop() #return the final node in the stack
    
    
        
#=============================================== Part III ==============================================

class AdvancedCalculator(Calculator):
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}
        Calculator.__init__(self)
        
    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if word[:1].isalpha() == True and word[1:].isalnum() == True: #check if the first character is a letter #check if the rest of the word is alphanumeric
            return True
        else:
            return False
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        if self._isNumber(expr) == True: #check if the expression is only a number
            return expr
        
        lst = expr.split()
        out = []
        op = ["+", "-", "*", "/", "^", "(", ")"]
        for element in lst:
            if element in self.states:
                out.append(str(self.states[element]))
            elif self._isNumber(element) == True:
                out.append(element)
            elif element in op:
                out.append(element)
            else:
                return None
        return ' '.join(out)

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        pass