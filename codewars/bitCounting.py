def betterCountBits(n):
    """
    Counts the number of ones in a given integer, n
    Same function as countBits(n), but uses built in binary conversion
    """
    return bin(n).count('1')


def countBits(n):
    """
    Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary
    representation of that number. You can guarantee that input is non-negative.
    """
    values = {} #keeps track of binary value for each position
    pos = 0
    count = 1
    while count <= n:
        values[pos] = count
        count *= 2
        pos += 1
    #binary = '' #string to represent binary output
    ones = 0
    for x in range(pos-1,-1,-1):
        if n >= values[x]:
            n -= values[x]
            ones += 1
            # converts to binary
            '''
            binary += '1'
        else:
            binary += '0'
            '''
    return ones

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
