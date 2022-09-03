def genFib(fn):
    '''
        >>> evens = genFib(lambda x: x % 2 == 0)
        >>> [next(evens) for _ in range(15)]
        [0, 2, 8, 34, 144, 610, 2584, 10946, 46368, 196418, 832040, 3524578, 14930352, 63245986, 267914296]
        >>> seq = genFib(lambda x: x > 20 and x % 2)
        >>> next(seq)
        21
        >>> next(seq)
        55
        >>> next(seq)
        89
        >>> next(seq)
        233
        >>> next(seq)
        377
        >>> next(seq)
        987
        >>> next(seq)
        1597
        >>> next(seq)
        4181
        >>> evens = genFib(lambda x: x % 2 == 0)
        >>> sum([next(evens) for _ in range(50)])
        3080657373857639014791750813074
        >>> odds = genFib(lambda x: x % 2 == 1)
        >>> [next(odds) for i in range(25)]
        [1, 1, 3, 5, 13, 21, 55, 89, 233, 377, 987, 1597, 4181, 6765, 17711, 28657, 75025, 121393, 317811, 514229, 1346269, 2178309, 5702887, 9227465, 24157817]
        >>> ends_with_5 = genFib(lambda x: x % 10 == 5)
        >>> [next(ends_with_5) for i in range(10)]
        [5, 55, 6765, 75025, 9227465, 102334155, 12586269025, 139583862445, 17167680177565, 190392490709135]

    '''
    # YOUR CODE STARTS HERE
    a = 0
    b = 1
    if fn(a) == True:
        yield(a)
    while b:
        if fn(b) == True:
            yield(b)
        temp = b
        b += a
        a = temp