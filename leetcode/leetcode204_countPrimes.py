class Solution():
    def __init__(self, n):
        self.n = n
        self.countPrimes(self.n)

    def countPrimes(self, n: int) -> int:
        """
        Counts the number of prime numbers less than a non negative number: n
        """
        primeCount = 1 #counts 1
        for i in range(1,n,2):
            if self.isPrime(i):
                primeCount += 1
        return primeCount

    def isPrime(self, x: int) -> bool:
        """
        Checks if a number is prime
        """
        if x < 2:
            return False
        while i ** 2 < x:
            if x % i == 0:
                return False
        return True


    """
    Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
    """
