class Solution():
    def __init__(self, n):
        self.n = n
        self.countPrimes(self.n)

    def countPrimes(self, n: int) -> int:
        """
        Counts the number of prime numbers less than a non negative number: n
        """
        if (n < 3):  # 2 is the first prime number
            return 0

        primelist = [1] * n  # make a list of all possible numbers, but remove 1 and current num
        primelist[0] = 0 #0 and 1 are always not prime
        primelist[1] = 0

        for x in range(2, int(n ** 0.5) + 1):  # goes from 2 to the square root of n
            if (primelist[x] == 1):  # skips if already set to 0
                for y in range(x * x, n, x):  # sets all multiples of current position index up to n to 0
                    primelist[y] = 0
        return sum(primelist)


    """
    Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
    """
