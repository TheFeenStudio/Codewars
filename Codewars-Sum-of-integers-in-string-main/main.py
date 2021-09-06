'''
Your task in this kata is to implement a function that calculates the sum of the integers inside a string.
For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.
Note: only positive integers will be tested.
'''
def sum_of_integers_in_string(s):
    num_list = []

    num = ''
    count = 0

    for i in s:
        if i.isdigit():
            num = num + i
        else:
            if num != '':
                num_list.append(int(num))
                count = count + int(num)
                num = ''
    if num != '':
        num_list.append(int(num))
        count = count + int(num)

    return count

sum_of_integers_in_string()
