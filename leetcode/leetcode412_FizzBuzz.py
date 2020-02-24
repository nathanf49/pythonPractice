"""
Write a program that outputs the string repressentation of numbers from 1 to n.
But for multiples of 3, it should output "Fizz" instead of the number and for multiples of five, output "Buzz"
For numbers that are multiples of both 3 and 5 output "FizzBuzz"
"""

def fizzBuzz(n):
    """
    Returns: List[strs]
    """
    out = []
    for i in range(1,n+1):
        if (i % 3 == 0) and (i % 5 == 0): #should be first because if either individual case is first it won't reach
            # both in if/elif/else
            out.append('FizzBuzz')
        elif i % 5 == 0:
            out.append('Buzz')
        elif i % 3 == 0:
            out.append('Fizz')
        else:
            out.append(str(i))
    return out


"""
Example:
n = 15
Return: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""