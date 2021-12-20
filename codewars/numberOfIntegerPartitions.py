"""
An integer partition of n is a weakly decreasing list of positive integers which sum to n.

For example, there are 7 integer partitions of 5:

[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].

Write a function named partitions which returns the number of integer partitions of n. The function should be able to find the number of integer partitions of n for n as least as large as 100.
"""

def partitions(n):
    i = [[n]] # integer partitions
    while len(i[-1]) < n: # last integer partition should always be a list of 1s
        for x in i:
            if max(x) > 1: # if any number is higher than 1 we add a partition lowering that number by 1 and adding a 1 to keep the same total
                k = x.copy()
                k.append(max(x)-1) # add new numbers (max-1,1)
                k.append(1)
                k.remove(max(x)) # remove replaced number
                i.append(k)
    print(i)
    return i

if __name__ == "__main__":
    partitions(5)


