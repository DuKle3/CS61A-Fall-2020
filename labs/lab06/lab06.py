this_file = __file__


def make_adder_inc(a):
    """
    >>> adder1 = make_adder_inc(5)
    >>> adder2 = make_adder_inc(6)
    >>> adder1(2)
    7
    >>> adder1(2) # 5 + 2 + 1
    8
    >>> adder1(10) # 5 + 10 + 2
    17
    >>> [adder1(x) for x in [1, 2, 3]]
    [9, 11, 13]
    >>> adder2(5)
    11
    """
    "*** YOUR CODE HERE ***"
    def helper(x):
        nonlocal a 
        a = a + 1 
        return x + a - 1

    return helper


def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    >>> from construct_check import check
    >>> # Do not use lists in your implementation
    >>> check(this_file, 'make_fib', ['List'])
    True
    """
    "*** YOUR CODE HERE ***"
    index = 0 
    def helper():
        nonlocal index
        def fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1 
            else:
                return fib(n - 1) + fib(n - 2)
        tmp = index
        index = index + 1 
        return fib(tmp)
    return helper

    """
    Another Solution
    x1 = -1 
    x2 = 1 
    def helper():
        nonlocal x1, x2 
        ret = x1 + x2 
        x1 = x2 
        x2 = ret 
        return ret
    return helper()
    """


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    i = 0
    while True:
        try:
            if lst[i] == entry:
                lst[i + 1: i + 1] = [elem]
                i += 2
            else:
                i += 1
        except IndexError:
            return lst

