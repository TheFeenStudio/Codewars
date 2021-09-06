"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""


def solution(s):
    list = [s[i:i+2] for i in range(0, len(s), 2)]

    try:
        if len(list[-1]) < 2:
            list[-1] = list[-1] + '_'
    except: IndexError

    return list

solution('x')