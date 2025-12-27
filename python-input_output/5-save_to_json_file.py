#!/usr/bin/python3

"""
This function for writing an Object to file using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """This function for writing an Object to file using a JSON representation"""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
