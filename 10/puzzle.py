# -*- coding: utf-8 -*-
"""
Created on Thu Dec  10 05:57:45 2021
@author: Marysia
Solution to puzzle from https://adventofcode.com/2021/day/10
"""

import statistics
import functools

def open_data(in_name):
    '''
    Opens the data for the puzzle.
    '''
    with open(in_name, 'r') as file:
        out_data = file.readlines()
    return tuple(x.strip() for x in out_data)

@functools.lru_cache(None)
def solve_puzzle(in_list):
    '''
    Solves two parts of the puzzle.
    '''
    score_dict = {')': 3,
                  ']': 57,
                  '}': 1197,
                  '>': 25137}
    points_to_add = {'(': 1,
                     '[': 2,
                     '{': 3,
                     '<': 4}
    score = 0
    total_score = []
    total_score_mltiplicator = 5
    for row in in_list:
        total_score_tmp = 0
        length_old = 0
        while len(row) != length_old:
            length_old = len(row)
            row = row.replace('()', '')
            row = row.replace('[]', '')
            row = row.replace('{}', '')
            row = row.replace('<>', '')
        if ')' in row or ']' in row or '}' in row or '>' in row:
            suspicuous_characters = [row.find(')'),
                                     row.find(']'),
                                     row.find('}'),
                                     row.find('>')]
            suspicuous_characters = [_ for _ in suspicuous_characters if _ != -1]
            illegal_character = row[min(suspicuous_characters)]
            score += score_dict[illegal_character]
        else:
            for char in row[::-1]:
                total_score_tmp = total_score_tmp*total_score_mltiplicator \
                                + points_to_add[char]
            total_score += [total_score_tmp]
    return score, statistics.median(total_score)


assert solve_puzzle(open_data('test.txt'))[0] == 26397
assert solve_puzzle(open_data('test.txt'))[1] == 288957

print(solve_puzzle(open_data('input.txt')))
