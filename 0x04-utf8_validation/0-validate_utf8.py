#!/usr/bin/python3
"""
validUTF8 method
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing 1 byte of data each

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    byte_count = 0
    for byte in data:
        if byte_count == 0:
            if (byte >> 5) == 0b110:
                byte_count = 1
            elif (byte >> 4) == 0b1110:
                byte_count = 2
            elif (byte >> 3) == 0b11110:
                byte_count = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
