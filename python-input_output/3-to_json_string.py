#!/usr/bin/python3

"""
This function is for writing to a file
"""
import json


def to_json_string(my_obj):
    """
    This function is for writing to a file
    """
    jsonfied_object = json.dumps(my_obj)
    return jsonfied_object
