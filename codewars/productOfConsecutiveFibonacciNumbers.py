def productFib(prod):
    fibSequence = [0, 1] # starting sequence
    while fibSequence[-2] * fibSequence[-1] <= prod: # runs until we get past prod, then we have to return False
        if fibSequence[-2] * fibSequence[-1] == prod: # return values and true if we get exactly prod
            return [fibSequence[-2], fibSequence[-1], True]
        else: # adds next fibonacci number to list if product of last 2 is less than prod
            fibSequence.append(fibSequence[-2] + fibSequence[-1])

    return [fibSequence[-2], fibSequence[-1], False] # return last 2 nums and False if we pass prod

"""
Examples:
productFib(4895), [55, 89, True]
productFib(5895), [89, 144, False]

The Fibonacci numbers are the numbers in the following integer sequence (Fn):

    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

such as

    F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.

Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

    F(n) * F(n+1) = prod.

Your function productFib takes an integer (prod) and returns an array:

[F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)

depending on the language if F(n) * F(n+1) = prod.

If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return

[F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)

F(m) being the smallest one such as F(m) * F(m+1) > prod.
Some Examples of Return:

(depend on the language)

productFib(714) # should return (21, 34, true), 
                # since F(8) = 21, F(9) = 34 and 714 = 21 * 34

productFib(800) # should return (34, 55, false), 
                # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
-----
productFib(714) # should return [21, 34, true], 
productFib(800) # should return [34, 55, false], 
-----
productFib(714) # should return {21, 34, 1}, 
productFib(800) # should return {34, 55, 0},        
-----
productFib(714) # should return {21, 34, true}, 
productFib(800) # should return {34, 55, false}, 

Note:

    You can see examples for your language in "Sample Tests".

"""