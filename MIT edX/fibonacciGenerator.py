def genFib():
    """
    generates the Fibonacci sequence to an unlimited length while yields are continued
    """
    fib1 = 1
    fib2 = 0
    while True:
        next = fib1 + fib2
        yield next  # python stops at a yield and returns the value. Program is resumed with __next__() method
        fib2 = fib1
        fib1 = next
x = genFib()
# x.__next__() #resumes after yield
