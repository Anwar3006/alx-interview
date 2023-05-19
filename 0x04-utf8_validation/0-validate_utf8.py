#!/usr/bin/python3
"""
UTF-8 validation module
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Checks if a list of integers are valid UTF-8 codepoints.
    """
    #Converts Array elements to their binary representation
    Binary = [] 
    for value in data:
        if len(f"{value:b}") < 8:
            Binary.append('0' + f"{value:b}")
        else:
            Binary.append(f"{value:b}")

    #Slice array to 4th element and slice new array elements to 4th digit
    SlicedList = []
    for element in Binary[:4]:
        SlicedList.append(element[:4])

    # Perform comparisons
    if SlicedList[0].startswith('01'):
        return True
    if SlicedList[0].startswith(
            '110') and SlicedList[1].startswith('10'):
        return True
    if SlicedList[0] == '1110' and SlicedList[1].startswith('10')\
            and SlicedList[2].startswith('10'):
        return True
    if SlicedList[0] == '1111' and SlicedList[1].startswith('10')\
            and SlicedList[2].startswith('10')\
            and SlicedList[3].startswith('10'):
        return True
    return False
