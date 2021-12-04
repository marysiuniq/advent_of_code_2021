# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 05:57:27 2021

@author: Marysia

Solution to puzzle from https://adventofcode.com/2021/day/4
"""

import numpy as np

def open_data(in_name):
    '''
    Opens the data for the puzzle.
    '''
    with open(in_name, 'r') as file:
        out_data = file.readlines()
    return [x.strip().split() for x in out_data]

def prepare_boards(in_list):
    '''
    Prepare bingo boards.
    '''
    boards = {}
    neg_sums_for_boards = {}
    index = 0
    for ind in range(2, len(in_list), 6):
        boards[index] = np.array(in_list[ind:ind+5]).astype(np.int)
        neg_sums_for_boards[index] = 0
        index += 1
    return boards, neg_sums_for_boards

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    boards, neg_sums_for_boards = prepare_boards(in_list)
    draw_numbers = in_list[0][0].split(',')
    for number in draw_numbers:
        for key in boards:
            if int(number) in boards[key]:
                boards[key][np.where(boards[key] == int(number))] = -1
                neg_sums_for_boards[key] += 1
                if (-5 in np.sum(boards[key], axis=0)
                        or -5 in np.sum(boards[key], axis=1)):
                    winning_board = key
                    sum_of_unmarked = np.sum(boards[winning_board])
                    sum_of_unmarked += neg_sums_for_boards[winning_board]
                    return sum_of_unmarked * int(number)
    return -1


def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    boards, neg_sums_for_boards = prepare_boards(in_list)
    draw_numbers = in_list[0][0].split(',')
    for number in draw_numbers:
        for key in list(boards.keys()):
            if int(number) in boards[key]:
                boards[key][np.where(boards[key] == int(number))] = -1
                neg_sums_for_boards[key] += 1
                if (-5 in np.sum(boards[key], axis=0)
                        or -5 in np.sum(boards[key], axis=1)):
                    if len(boards) != 1:
                        del boards[key]
                        continue
                    winning_board = key
                    sum_of_unmarked = np.sum(boards[winning_board])
                    sum_of_unmarked += neg_sums_for_boards[winning_board]
                    return sum_of_unmarked * int(number)
    return -1

assert solve_part_one(open_data('test.txt')) == 4512
assert solve_part_two(open_data('test.txt')) == 1924

print(solve_part_one(open_data('input.txt')))
print(solve_part_two(open_data('input.txt')))
