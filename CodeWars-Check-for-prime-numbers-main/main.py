'''
In this kata you will create a function to check a non-negative input to see if it is a prime number.

The function will take in a number and will return True if it is a prime number and False if it is not.

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Examples(input --> output)
0 --> false
1 --> false
2 --> true
11 --> true
12 --> false
'''

def IsPrime(n):
    count = 0
    if n > 1:
        if n % 1 == 0 and n % n == 0:
            for i in range(n + n):
                if i != 0:
                    if n % i == 0:
                        count = count + 1
            if count == 2:
                return True
            else:
                return False
    else:
        return False
