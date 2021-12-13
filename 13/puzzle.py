# -*- coding: utf-8 -*-
"""
Created on Thu Dec  13 06:03:21 2021
@author: Marysia
Solution to puzzle from https://adventofcode.com/2021/day/13
"""
import matplotlib.pyplot as plt

def open_data(in_name):
    '''
    Opens the data for the puzzle.
    '''
    with open(in_name, 'r') as file:
        out_data = file.readlines()
    return [x.strip() for x in out_data]

def make_folds(in_list):
    '''
    This function makes folds for you.
    '''
    limit_pos = in_list.index('')
    positions = [(int(_[0:_.find(',')]), int(_[_.find(',')+1:])) for _ in in_list[0:limit_pos]]
    fold_list = [[_[11:12], int(_[13:])] for _ in in_list[limit_pos+1:]]
    dots_in_paper = []
    for fold in fold_list:
        if fold[0] == 'y':
            for dot_ind, dot in enumerate(positions):
                if dot[1] > fold[1]:
                    positions[dot_ind] = (positions[dot_ind][0], 2*fold[1] - dot[1])
        elif fold[0] == 'x':
            for dot_ind, dot in enumerate(positions):
                if dot[0] > fold[1]:
                    positions[dot_ind] = (2*fold[1] - dot[0], positions[dot_ind][1])
        dots_in_paper += [len(set(positions))]
    return dots_in_paper, positions


def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    dots_in_paper, _ = make_folds(in_list)
    return dots_in_paper[0]

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    _, positions = make_folds(in_list)
    x_pos = [_[0] for _ in positions]
    y_pos = [-_[1] for _ in positions]
    plt.scatter(x_pos, y_pos)
    plt.axis('equal')
    plt.show()

assert solve_part_one(open_data('test.txt')) == 17

print(solve_part_one(open_data('input.txt')))
print(solve_part_two(open_data('input.txt')))
