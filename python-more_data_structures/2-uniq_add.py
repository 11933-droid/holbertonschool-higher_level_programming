#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_numbers = set(my_list)
    total = 0
    for num in uniq_numbers:
        total += num
    return total
