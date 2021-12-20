import sys

def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number)
    return number

if __name__ == '__main__':
    try:
        foo = int(input('Enter number:'))
    except:
        print('You must enter an integer')
        sys.exit()
    while foo != 1:
        foo = collatz(foo)
