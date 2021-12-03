# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:08:10 2021

@author: Marysia

Solution to puzzle from https://adventofcode.com/2021/day/3
"""

def open_data(in_name):
    '''
    Opens the data for the puzzle.
    '''
    with open(in_name, 'r') as file:
        out_data = file.readlines()
    return [x.strip() for x in out_data]

def solve_part_one(in_list):
    '''
    Solves part one.
    '''
    gamma, epsilon = get_epsilon_and_gamma(in_list)
    return int(epsilon, 2) * int(gamma, 2)

def get_epsilon_and_gamma(in_list):
    '''
    Computes epsilon and gamma based on bits in input.
    '''
    line_len = len(in_list[0])
    input_len = len(in_list)
    gamma = ''
    epsilon = ''
    for i in range(line_len):
        el_sum = 0
        for j in in_list:
            el_sum += int(j[i])
        if el_sum >= input_len/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return gamma, epsilon

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    oxygen = in_list
    co2 = in_list
    gamma, epsilon = get_epsilon_and_gamma(in_list)
    line_len = len(in_list[0])
    for i in range(line_len):
        if len(oxygen) > 1:
            oxygen = [_ for _ in oxygen if _[i] == gamma[i]]
            gamma, _ = get_epsilon_and_gamma(oxygen)
        if len(co2) > 1:
            co2 = [_ for _ in co2 if _[i] == epsilon[i]]
            _, epsilon = get_epsilon_and_gamma(co2)
    return int(oxygen[0], 2) * int(co2[0], 2)

assert solve_part_one(open_data('test.txt')) == 198
assert solve_part_two(open_data('test.txt')) == 230

print(solve_part_one(open_data('input.txt')))
print(solve_part_two(open_data('input.txt')))
