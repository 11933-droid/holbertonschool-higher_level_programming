#!/usr/bin/python3

''' This module for class creation that serelize and deserize it self as instance'''

import pickle



class CustomObject():
    

    def __init__(self, name = "", is_student = False, age = 0):
        self.name =name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        try:
            with open(filename,"wb") as file:
                pickle.dump(self,file)
        except:
            return None
    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename,"rb") as file:
                return pickle.load(file)
        except:
            return None
