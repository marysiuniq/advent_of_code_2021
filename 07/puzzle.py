# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 05:58:39 2021

@author: Marysia

Solution to puzzle from https://adventofcode.com/2021/day/7
"""

import numpy as np

def open_data(in_name):
    '''
    Opens the data for the puzzle.
    '''
    with open(in_name, 'r') as file:
        out_data = file.readlines()
        out_data = out_data[0].split(',')
    return [int(x) for x in out_data]

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    lowest_fuel_position = np.median(in_list)
    return int(sum([np.abs(list_1 - list_2) for list_1, list_2
                    in zip(in_list, [lowest_fuel_position]*len(in_list))]))

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    lowest_fuel_position = round(sum(in_list)/len(in_list))
    list_to_check = []
    for num in range(lowest_fuel_position-1, lowest_fuel_position+1):
        list_zip = [num]*len(in_list)
        list_to_check = np.append(list_to_check,
                                  sum([np.abs(list_1 - list_2)
                                       *(np.abs(list_1 - list_2)+1)/2
                                       for list_1, list_2
                                       in zip(in_list, list_zip)]))
    return int(min(list_to_check))

assert solve_part_one(open_data('test.txt')) == 37
assert solve_part_two(open_data('test.txt')) == 168
assert solve_part_two(open_data('data_adv_2021_07_p.txt')) == 90040997

print(solve_part_one(open_data('input.txt')))
print(solve_part_two(open_data('input.txt')))
