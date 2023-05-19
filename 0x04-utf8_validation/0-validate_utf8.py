#!/usr/bin/python3
"""
UTF-8 validation module
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Checks if a list of integers are valid UTF-8 codepoints.
    """
    Sliced_Binary = slice_it(convert_to_binary(data))

    if Sliced_Binary[0].startswith('01'):
        return True
    if Sliced_Binary[0].startswith(
            '110') and Sliced_Binary[1].startswith('10'):
        return True
    if Sliced_Binary[0] == '1110' and Sliced_Binary[1].startswith('10')\
            and Sliced_Binary[2].startswith('10'):
        return True
    if Sliced_Binary[0] == '1111' and Sliced_Binary[1].startswith('10')\
            and Sliced_Binary[2].startswith('10')\
            and Sliced_Binary[3].startswith('10'):
        return True
    return False


def convert_to_binary(array):
    """
    Converts Array elements to their binary representation
    """
    new_list = []
    for value in array:
        if len(f"{value:b}") < 8:
            new_list.append('0' + f"{value:b}")
        else:
            new_list.append(f"{value:b}")
    return new_list


def slice_it(array):
    """
    Slice array to 4th element and slice new array elements to 4th digit
    """
    new_list = []
    for element in array[:4]:
        new_list.append(element[:4])
    return new_list
