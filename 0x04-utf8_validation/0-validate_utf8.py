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

    # Iterate over each byte in the data
    i = 0
    while i < len(data):
        # Check for ASCII character
        if data[i] < 128:
            i += 1
            continue
        # Check for two-byte sequence
        elif 194 <= data[i] <= 223:
            if i + 1 >= len(data) or not 128 <= data[i+1] <= 191:
                return False
            i += 2
        # Check for three-byte sequence
        elif 224 <= data[i] <= 239:
            if i + 2 >= len(data) or not \
                    all(128 <= x <= 191 for x in data[i+1:i+3]):
                return False
            i += 3
        # Check for four-byte sequence
        elif 240 <= data[i] <= 244:
            if i + 3 >= len(data) or not \
                    all(128 <= x <= 191 for x in data[i+1:i+4]):
                return False
            i += 4
        # Invalid byte
        else:
            return False
    return True
