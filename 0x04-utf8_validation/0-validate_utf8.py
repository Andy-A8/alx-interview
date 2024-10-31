#!/usr/bin/python3
"""
    Write a method that determines if a given data set represents a valid
    UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to handle
    the 8 least significant bits of each integer
"""


def validUTF8(data):
    num_bytes = 0

    for num in data:
        # Get the last 8 bits of the integer to check the byte
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine how many bytes this character will use
            if (byte & 0x80) == 0:
                # 1-byte character (0xxxxxxx)
                num_bytes = 0
            elif (byte & 0xE0) == 0xC0:
                # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte & 0xF0) == 0xE0:
                # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                return False
        else:
            # If we're in the middle of a multi-byte character
            if (byte & 0xC0) != 0x80:
                # The continuation byte must start with '10xxxxxx'
                return False
            num_bytes -= 1

    return num_bytes == 0
