#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

# data = [65]
# print(validUTF8(data))

# data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
# print(validUTF8(data))

# data = [229, 65, 127, 256]
# print(validUTF8(data))

data = [467, 133, 108]
print(validUTF8(data))

data = [240, 188, 128, 167]
print(validUTF8(data))

data = [235, 140]
print(validUTF8(data))

# def slice_it(array):
#     """
#     Slice array to 4th element and slice new array elements to 4th digit
#     """
#     new_list = []

# def convert_to_binary(array):
#     """
#     Converts Array elements to their binary representation
#     """
#     new_list = []

#     return new_list