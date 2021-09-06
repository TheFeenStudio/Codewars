"""
Task
A masked number is a string that consists of digits and one asterisk (*) that should be replaced by exactly one digit. Given a masked number s, find all the possible options to replace the asterisk with a digit to produce an integer divisible by 6.

Input/Output
[input] string s

A masked number.

1 ≤ inputString.length ≤ 10000.

[output] a string array

Sorted array of strings representing all non-negative integers that correspond to the given mask and are divisible by 6.

Example
For s = "1*0", the output should be ["120", "150", "180"].

For s = "*1", the output should be [].

For s = "1234567890123456789012345678*0",
"""
def is_divisible_by_6(s):
    matched = []
    for i in range(10):

        if i == 0 and int(s.replace('*', str(i))) % 6 == 0:
            if len(s.replace('*', str(i))) != 1 and int(s.replace('*', str(i))[:1]) == 0:
                matched.append(s.replace('*', ''))
            else:
                matched.append(s.replace('*', '0'))
        if int(s.replace('*', str(i))) % 6 == 0 and i != 0:
            matched.append(s.replace('*', str(i)))

    print(matched)

is_divisible_by_6("1*0")
