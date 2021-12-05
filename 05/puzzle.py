# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 06:00:16 2021

@author: Marysia

Solution to puzzle from https://adventofcode.com/2021/day/5
"""

import numpy as np

def open_data(in_name):
    '''
    Opens the data for the puzzle.
    '''
    with open(in_name, 'r') as file:
        out_data = file.readlines()
    return [x.strip() for x in out_data]

def make_grid_with_vertical_and_horizontal_lines(from_x1, from_x2, from_y1, from_y2):
    '''
    Prepares the grid with marked lines.
    '''
    grid = [[0 for col in range(max(max(from_x1), max(from_x2))+1)]
            for row in range(max(max(from_y1), max(from_y2))+1)]
    same_x = [from_x1[_] == from_x2[_] for _ in range(len(from_x1))] # indicate vertical lines
    same_y = [from_y1[_] == from_y2[_] for _ in range(len(from_y1))] # indicate horisontal lines
    true_x = [_ for _ in range(len(same_x)) if same_x[_]]
    true_y = [_ for _ in range(len(same_y)) if same_y[_]]
    for x_pos in true_x:
        for y_cur in  range(min(from_y1[x_pos], from_y2[x_pos]),
                            max(from_y1[x_pos], from_y2[x_pos])+1):
            grid[y_cur][from_x1[x_pos]] += 1
    for y_pos in true_y:
        for x_cur in  range(min(from_x1[y_pos], from_x2[y_pos]),
                            max(from_x1[y_pos], from_x2[y_pos])+1):
            grid[from_y1[y_pos]][x_cur] += 1
    return grid

def find_coordinates(in_list):
    '''
    Extracts coordinates from input list
    '''
    x_out = [int(_[0:_.find(',')]) for _ in in_list]
    y_out = [int(_[_.find(',')+1:]) for _ in in_list]
    return x_out, y_out

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    x_1, y_1 = find_coordinates([_[0:_.find(' ')] for _ in in_list])
    x_2, y_2 = find_coordinates([_[_.find(' ')+4:] for _ in in_list])
    grid = make_grid_with_vertical_and_horizontal_lines(x_1, x_2, y_1, y_2)
    return sum(sum(np.array(grid) >= 2))

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    x_1, y_1 = find_coordinates([_[0:_.find(' ')] for _ in in_list])
    x_2, y_2 = find_coordinates([_[_.find(' ')+4:] for _ in in_list])
    grid = make_grid_with_vertical_and_horizontal_lines(x_1, x_2, y_1, y_2)
    true_diagonal = [_ for _ in range(len(x_1))
                     if (x_1[_]-y_1[_] == x_2[_]-y_2[_]
                         or x_1[_]+y_1[_] == x_2[_]+y_2[_])]
    for ind in true_diagonal:
        slope = int((y_1[ind]-y_2[ind])/(x_1[ind]-x_2[ind]))
        intercept = int(y_1[ind] - slope * x_1[ind])
        for x_cur in range(x_1[ind], x_2[ind] + np.sign(x_2[ind]-x_1[ind]),
                           np.sign(x_2[ind]-x_1[ind])):
            grid[slope*x_cur+intercept][x_cur] += 1
    return sum(sum(np.array(grid) >= 2))

assert solve_part_one(open_data('test.txt')) == 5
assert solve_part_two(open_data('test.txt')) == 12

print(solve_part_one(open_data('input.txt')))
print(solve_part_two(open_data('input.txt')))
