class Complex:
    """ Complex number of the form a + bi, where a and b are real numbers, and i is an indeterminate satisfying i2 = −1 """

    def __init__(self,r,i):
        self._real = r
        self._imag = i
        

    def __str__(self):
        """Display complex number"""
        if self._imag>=0:
            return f"{self._real} + {self._imag}i"
        else:
            return f"{self._real} - {abs(self._imag)}i"

    __repr__ = __str__
    
    def conjugate(self):
        """Returns a Complex object that represents the complex conjugate"""
        if self._imag<=0:
            z = Complex(self._real, abs(self._imag))
            return z
        else:
            z = Complex(self._real, neg(self._imag))
            return z
    
    def __mul__(self,other):
        """Multiply two Complex numbers"""
        #re = (self._real * other._real) - (self._imag * other._imag)
        #im = (self._real * other._imag) + (self._imag * other._real)
        #ans = Complex(re, im)
        #ans = Complex(((self._real * other._real) - (self._imag * other._imag)),((self._real * other._imag) + (self._imag * other._real)))
        if isinstance(other, Complex):
            ans = Complex(((self._real * other._real) - (self._imag * other._imag)),((self._real * other._imag) + (self._imag * other._real)))
        else:
            ans = Complex((self._real * other), (self._imag * other))
        return ans

    def __rmul__(self,other):
        """Multiply a real and Complex number"""
        #ans = Complex((self * other._real), (self * other._imag))
        ans = Complex((self._real * other), (self._imag * other))
        return ans

class Real(Complex):

    def __init__(self, value):
        super().__init__(value, 0)

    def __mul__(self,other):
        if isinstance(other, Real) == True:
            ans = Real((self._real * other._real))
        elif isinstance(other, int) == True: 
            ans = Real((self._real * other))
        elif isinstance(other, float) == True: 
            ans = Real((self._real * other))
        elif isinstance(other, Complex) == True:
            ans = Complex.__mul__(self, other)
        return ans

    def __rmul__(self,other):
        ans = Real(self._real * other)
        return ans

    def __eq__(self, other):

        ''' Returns True if other is a Real object that has the same value or if other is
            a Complex object with _imag=0 and same value for _real, False otherwise

            >>> Real(4) == Real(4)
            True
            >>> Real(4) == Real(4.0)
            True
            >>> Real(5) == Complex(5, 0)
            True
            >>> Real(5) == Complex(5, 12)
            False
            >>> Real(5) == 5.5
            False
        '''
        # YOUR CODE STARTS HERE
        if isinstance(other, Real) == True:
            if self._real == other._real:
                return True
            else: 
                return False
        elif isinstance(other, Complex) == True:
            if self._real == other._real and other._imag == 0:
                return True
            else:
                return False
        else:
            return False

    def __int__(self):
        return int(self._real)

    def __float__(self):
        return float(self._real)

if __name__ == "__main__":
    import doctest
    doctest.testmod()