# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 18:44:39 2021

@author: Marysia

Puzzle 1 from https://adventofcode.com/2021/day/1
"""

import numpy as np

def solve_part_one(in_list):
    '''
    Solves part one: counts the number of increments.
    '''
    result = 0
    for i, number in enumerate(in_list[:-1]):  # note 1
        if in_list[i+1] - number > 0:
            result += 1
    return result

def solve_part_two(in_list):
    '''
    Solves part two: counts the number of increments of the sums
    of three successive elements.
    '''
    result = 0
    for i, _ in enumerate(in_list[:-3]):  # note 1
        if np.sum(in_list[i+1:i+4]) > np.sum(in_list[i:i+3]):
            result += 1
    return result

with open('input.txt', 'r') as file:
    NUMBERS = file.readlines()

NUMBERS = [int(x.strip()) for x in NUMBERS]

print(solve_part_one(NUMBERS))
print(solve_part_two(NUMBERS))
