class Solution:
    def addStrings(num1: str, num2: str) -> str:
        total = ''
        carryover = 0  # used for adding since we're going position by position
        if len(num1) >= len(num2):
            long = num1
            short = num2
        else:
            long = num2
            short = num1

        n = len(long) - len(short)
        short = n * '0' + short  # fills in 0s to make the strings the same length

        for i in range(len(short),0,-1):
            d = int(long[i-1]) + int(short[i-1]) + carryover  # adds carryover from previous index
            carryover = 0  # clears carryover so it can be set again
            if d > 9:
                d, carryover = carryoverCalc(d)  # carries over value from d
            total = str(d) + total

        if carryover != 0:
            total = str(carryover) + total

        return total


def carryoverCalc(total):
    for x in range(10, 100, 10):
        if total - x < 10:
            return total - x, int(x/10)
        
if __name__ == "__main__":
    a,b= 456,77
    print('Function: ' + str(Solution.addStrings(str(a),str(b))))
    print('Answer: ' + str(a+b))