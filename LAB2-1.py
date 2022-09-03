# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

from cmath import inf
import random

class Fibonacci:
    """
        >>> fib_seq = Fibonacci()
        >>> fib_seq
        <Fibonacci object>, value = 0
        >>> fib_seq.next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next().next()
        <Fibonacci object>, value = 3
        >>> fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
        >>> other_fib_seq = Fibonacci()
        >>> other_fib_seq
        <Fibonacci object>, value = 0
        >>> other_fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
    """

    def __init__(self):
        self.start = 0 


    def next(self):
        #--- YOUR CODE STARTS HERE
        fib_seq2 = Fibonacci() #creating another instance so .next can be called in succession
        if self.start == 0:    #starting the first instance (exception) of the fibonacci sequence
            fib_seq2.start = 1
            fib_seq2.prev = 0
        else:
            fib_seq2.start = self.prev + self.start #adding the current value to the previous value
            fib_seq2.prev = self.start
        return fib_seq2
        


    def __repr__(self):
        return f"<Fibonacci object>, value = {self.start}"


class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10'
        >>> east_machine.cancelTransaction()
        'Take your $10 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''

    def __init__(self):
        #--- YOUR CODE STARTS HERE
        self.dic = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]} #dictionary with code: cost, stock
        self.bal = 0 #creating balance attribute
        pass



    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE
        if item not in self.dic: #check if the item is in the dict
            return f"Invalid item"
        elif self.dic[156][1] == 0 and self.dic[254][1] == 0 and self.dic[384][1] == 0 and self.dic[879][1] == 0: #check stock of all items
            return f"Machine out of stock"
        elif self.dic[item][1] == 0: #check stock of item
            return f"Item out of stock"
        elif self.dic[item][1] < qty: #check if there is enough stock for the purchase
            return f"Current {item} stock: {self.dic[item][1]}, try again"
        elif (self.dic[item][0]*qty) > self.bal: #check if they put in enough money
            self.rem = (self.dic[item][0] * qty) - self.bal
            return f"Please deposit ${self.rem}" 
        elif (self.dic[item][0]*qty) == self.bal: #if they have exactly enough money and there is stock
            self.bal = 0
            self.dic[item][1] -= qty
            return f"Item dispensed"
        elif (self.dic[item][0]*qty) < self.bal: #if there is stock and they have extra money
            self.temp = self.bal - (self.dic[item][0]*qty)
            self.bal = 0
            self.dic[item][1] -= qty
            return f"Item dispensed, take your ${self.temp} back"
        


    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        self.bal += amount #adding money
        if self.dic[156][1] == 0 and self.dic[254][1] == 0 and self.dic[384][1] == 0 and self.dic[879][1] == 0: #checking the machine's stock
            return f"Machine out of stock. Take your ${self.bal} back"
        else:
            return f"Balance: ${self.bal}"


    def _restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        if item not in self.dic: #check if item is in the dict
            return f"Invalid item"
        else: 
            self.dic[item][1] += stock #adding stock to the items
            return f"Current item stock: {self.dic[item][1]}"


    #--- YOUR CODE STARTS HERE
    @property
    def isStocked(self): #checing stock of each item
        for key in self.dic:
            if self.dic[key][1] > 0:
                return True
        return False
        

    #--- YOUR CODE STARTS HERE
    @property
    def getStock(self): 
        return self.dic

    def cancelTransaction(self):
        #--- YOUR CODE STARTS HERE
        if self.bal == 0: 
            return None
        else:
            self.temp = self.bal #give back money
            self.bal = 0
            return f"Take your ${self.temp} back"
       
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __mul__(self, k):
        return Point2D(self.x * k, self.y * k) # multiplying the points

    __rmul__ = __mul__

class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = 4*line1
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
    '''
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.pt1 = point1           #creating the attributes with point values
        self.pt2 = point2

    #--- YOUR CODE STARTS HERE
    @property
    def getDistance(self):
        x = (self.pt1.x - self.pt2.x)**2  #pythagorean theorm
        y = (self.pt1.y-self.pt2.y)**2
        self.dist = round(((x+y)**.5), 3)
        return self.dist
       
    
    #--- YOUR CODE STARTS HERE
    @property
    def getSlope(self):
        x = self.pt2.x - self.pt1.x  #difference in x
        y = self.pt2.y - self.pt1.y  #difference in y
        if x == 0:
            return float(inf)  #for undefined
        slope = y/x
        self.slope = round(slope, 3) 
        return self.slope
        


    #--- YOUR CODE CONTINUES HERE
    
    def __str__(self):
        b = (self.pt1.y)-(self.pt1.x * self.getSlope) #solve for b
        b = abs(round(b, 3))
        self.b = round(b, 3)
        if self.getSlope == float(inf): #if undfined slope
            return "Undefined"
        if self.b == 0: #if no b
            return "y = {}x".format(self.getSlope)
        if self.getSlope == 0 and self.b == 0: #if no slope and b
            return "y = 0"
        if self.getSlope == 0: #if slope is 0
            return "y = {}".format(self.b)
        if self.b > 0: #if b is greater than 0
            return "y = {}x + {}".format(self.getSlope, self.b)
        if self.b < 0: #if b is less that 0
            return "y = {}x - {}".format(self.getSlope, b)
    __repr__ = __str__
    
    def __eq__(self, other):
        if str(self) == str(other): #comparing the 2 objects
            return True
        else:
            return False

    def __mul__(self, k):
        return Line(self.pt1*k, self.pt2*k) #multiplying the points

    __rmul__ = __mul__ #reverse mul




if __name__=='__main__':
    import doctest
    doctest.testmod()
    doctest.run_docstring_examples(Line, globals(), name='lab2',verbose=True) # replace Fibonacci for the class name you want to test