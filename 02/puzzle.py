# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 20:27:25 2021

@author: Marysia

Solution to puzzle from https://adventofcode.com/2021/day/2
"""

def open_data(in_name):
    '''
    Opens the data for the puzzle.
    '''
    with open(in_name, 'r') as file:
        out_data = file.readlines()
    return [x.strip().split() for x in out_data]

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    horisontal_pos = 0
    depth = 0
    for i in in_list:
        if i[0] == "forward":
            horisontal_pos += int(i[1])
        elif i[0] == "up":
            depth -= int(i[1])
        elif i[0] == "down":
            depth += int(i[1])
        else:
            continue
    return horisontal_pos * depth

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    horisontal_pos = 0
    depth = 0
    aim = 0
    for i in in_list:
        if i[0] == "forward":
            horisontal_pos += int(i[1])
            depth += aim * int(i[1])
        elif i[0] == "up":
            aim -= int(i[1])
        elif i[0] == "down":
            aim += int(i[1])
        else:
            continue
    return horisontal_pos * depth

assert solve_part_one(open_data('test.txt')) == 150
assert solve_part_two(open_data('test.txt')) == 900

print(solve_part_one(open_data('input.txt')))
print(solve_part_two(open_data('input.txt')))
