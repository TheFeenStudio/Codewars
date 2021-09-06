"""
Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).

Each 8 bits on the binary string represent 1 character on the ASCII table.

The input string will always be a valid binary string.

Characters can be in the range from "00000000" to "11111111" (inclusive)

Note: In the case of an empty binary string your function should return an empty string.
"""

def binary_to_string(binary):
    if binary == '':
        print('')
    else:
        n = int(binary, 2)
        print(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', binary) or '\0')

binary_to_string('00110001001100000011000100110001')
