def last_digit(lst):
    if lst == []: # corner cases
        return 1
    elif lst == [0,0]:
        return 1
    else: # all other cases
        lst[-1] = int(str(lst[-1])[-1])
        while len(lst) > 1: # second to last case to the last digit of last number gives same last digit
            lst[-2] = int(str(lst[-2] ** lst[-1])[-1])
            lst = lst[:-1]
        return int(str(lst[0])[-1]) # return last digit of last number

"""
For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

E. g.,

last_digit([3, 4, 2]) == 1

because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.

Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.

test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
]
"""