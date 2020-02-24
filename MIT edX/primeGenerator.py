def primeGenerator():
    n = 1 #n starts at 1
    while True: #infinite loop
        n += 1
        isPrime = True
        for divisor in range(2,n): #divior must be between 1 and n, skips even number
            if n % divisor == 0: #if there is no remainder dividing n by divisor it divides evenly so not prime
                isPrime = False
                break
        if isPrime == True:
            yield n
x = primeGenerator()