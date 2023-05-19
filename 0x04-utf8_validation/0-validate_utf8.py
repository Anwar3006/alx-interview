#!/usr/bin/python3
# """
# UTF-8 Validation Function
# """
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Check if elements in array:data constitute a valid UTF-8 encoding
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
            and Sliced_Binary[2].startswith('10'):
        return True
    return False


def convert_to_binary(array: List[int]) -> List[str]:
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


def slice_it(array: List[str]) -> List[str]:
    """
    Slice array to 4th element and slice new array elements to 4th digit
    """
    new_list = []
    for element in array[:4]:
        new_list.append(element[:4])
    return new_list
