"""
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764.
The sum of the squared divisors is 2500 which is 50 * 50, a square!
Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is
itself a square. 42 is such a number. The result will be an array of arrays or of tuples (in C an array of Pair) or a
string, each subarray having two elements, first the number whose squared divisors is a square and then the sum of the squared divisors.
"""


def list_squared(m, n):
    out = []
    for x in range(m, n):
        print(x) # just to check where we're at
        sumOfSquaredDivisorsRoot = divisorsSquaredSum(x) ** 0.5
        if sumOfSquaredDivisorsRoot == int(sumOfSquaredDivisorsRoot):  # checks if sumofSquaredDivisorsRoot is a square
            out.append([x, int(sumOfSquaredDivisorsRoot ** 2)])  # appends a list including the number whose squared divisors
            # is a square and then the sum of the squared divisors to out
    return out


def divisorsSquaredSum(x):
    out = []
    for i in range(1, x + 1):  # tries every possible divisor from 1 to x
        if x / i == int(x / i):  # checks if the int cast is the same to make sure it's a whole number
            if i ** 2 not in out:  # all i and int(x,i) are pairs, so checking for 1 checks for both
                out.append(i ** 2)  # saves divisors
            if int(x / i) ** 2 not in out:
                out.append(int(x / i) ** 2)
    return sum(out)


test = list_squared(1,25000)
print(test)
"""
#Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
"""
