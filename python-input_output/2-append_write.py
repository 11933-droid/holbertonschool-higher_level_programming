#!/usr/bin/python3

"""
This function is for writing to a file
"""


def append_write(filename="", text=""):
    """
    This function is for writing to a file
    """

    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
