#!/usr/bin/python3
"""This function for craeting json from class dictionary"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            filtered_list = {
                key: value for key, value in
                self.__dict__.items() if key in attrs
            }
            return filtered_list

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
