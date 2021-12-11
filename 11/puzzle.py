# -*- coding: utf-8 -*-
"""
Created on Thu Dec  11 06:05:15 2021
@author: Marysia
Solution to puzzle from https://adventofcode.com/2021/day/11
"""
import numpy as np

def open_data(in_name):
    '''
    Opens the data for the puzzle.
    '''
    with open(in_name, 'r') as file:
        out_data = file.readlines()
    return [x.strip() for x in out_data]

def input_to_array(in_list):
    '''
    Transforms input to array.
    '''
    list_out = []
    for row in in_list:
        list_out.append([int(x) for x in row])
    return list_out

def increase_surroundings(in_list, row_ind, column_ind):
    '''
    Increases the values of octopuses surrounding the exploded one.
    '''
    add_row = [-1, 0, 0, 1, -1, -1, 1, 1]
    add_column = [0, -1, 1, 0, -1, 1, 1, -1]
    for r_ind, c_ind in zip(add_row, add_column):
        if all([row_ind+r_ind >= 0, column_ind+c_ind >= 0, row_ind+r_ind < len(in_list[0]),
                column_ind+c_ind < len(in_list)]):
            if in_list[row_ind+r_ind, column_ind+c_ind] != 0:
                in_list[row_ind+r_ind, column_ind+c_ind] += 1
    return in_list

def solve_part_one(in_list, steps):
    '''
    Solves part one.
    '''
    in_list = input_to_array(in_list)
    increment_table = np.ones([len(in_list), len(in_list[0])])
    total_flashes = 0
    for _ in range(steps):
        in_list = in_list + increment_table
        change_made = 1
        while change_made == 1:
            change_made = 0
            for row_ind, row in enumerate(in_list):
                for column_ind, item in enumerate(row):
                    if item > 9:
                        in_list[row_ind, column_ind] = 0
                        change_made = 1
                        in_list = increase_surroundings(in_list, row_ind, column_ind)
        for item in np.nditer(in_list):
            if item == 0:
                total_flashes += 1
    return total_flashes

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    in_list = np.array(input_to_array(in_list))
    increment_table = np.ones([len(in_list), len(in_list[0])])
    step = 1
    while True:
        total_flashes = 0
        in_list = in_list + increment_table
        change_made = 1
        while change_made == 1:
            change_made = 0
            for row_ind, row in enumerate(in_list):
                for column_ind, item in enumerate(row):
                    if item > 9:
                        in_list[row_ind, column_ind] = 0
                        change_made = 1
                        in_list = increase_surroundings(in_list, row_ind, column_ind)
        for item in np.nditer(in_list):
            if item == 0:
                total_flashes += 1
        if total_flashes == len(in_list)*len(in_list[0]):
            return step
        step += 1
    return -1

assert solve_part_one(open_data('test.txt'), 100) == 1656
assert solve_part_two(open_data('test.txt')) == 195

print(solve_part_one(open_data('input.txt'), 100))
print(solve_part_two(open_data('input.txt')))
