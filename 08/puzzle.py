# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 06:06:18 2021
@author: Marysia
Solution to puzzle from https://adventofcode.com/2021/day/8
"""
import copy

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
    counter = 0
    start_pos = in_list[0].find('|') + 2
    digits = [_[start_pos:] for _ in in_list]
    for ind in range(0,len(digits)):
        for digit in digits[ind].split(' '):
            if len(digit) in [2,3,4,7]:
                counter += 1
    return counter

def split(word):
    return [char for char in word]

def solve_part_two(in_list):
    '''
    Solves part two.
    '''
    final_sum = 0;
    for entry in in_list:
        numbers_map = {0: [0, 1,2,4,5,6],
                   1: [2,5],
                   2: [0,2,3,4,6],
                   3: [0,2,3,5,6],
                   4: [1,2,3,5],
                   5: [0,1,3,5,6],
                   6: [0,1,3,4,5,6],
                   7: [0,2,5],
                   8: [0,1,2,3,4,5,6],
                   9: [0,1,2,3,5,6]}
        segments_map = {0: '',
                    1: '',
                    2: '',
                    3: '',
                    4: '',
                    5: '',
                    6: ''}
        patterns = entry[0:entry.find('|')-1].split(' ')
        numbers = entry[entry.find('|')+2:].split(' ')
        numbers_map[1] = set([split(_) for _ in patterns if len(_)==2][0])
        numbers_map[7] = set([split(_) for _ in patterns if len(_)==3][0])
        numbers_map[4] = set([split(_) for _ in patterns if len(_)==4][0])
        numbers_map[8] = set([split(_) for _ in patterns if len(_)==7][0])
        segments_map[0] = numbers_map[7].difference(numbers_map[1])
        nine_guess = [set(_) for _ in patterns if len(_)==6]
        for element in nine_guess:
            if len(element.intersection(numbers_map[4])) == 4:
                numbers_map[9] = element
                break
        segments_map[4] = numbers_map[8].difference(numbers_map[9])
        segments_map[6] = numbers_map[9].difference(numbers_map[4] | segments_map[0])
        six_and_zero = [set(_) for _ in patterns if len(numbers_map[8].difference(set(_)))==1 and set(_)!=numbers_map[9]]
        if len(six_and_zero[0].intersection(numbers_map[1])) == 1:
            numbers_map[6] = six_and_zero[0]
            numbers_map[0] = six_and_zero[1]
        else:
            numbers_map[6] = six_and_zero[1]
            numbers_map[0] = six_and_zero[0]
        patterns_tmp = copy.copy(patterns)
        for element in patterns:
            if set(element) in numbers_map.values():
                patterns_tmp.remove(element)
        for element in patterns_tmp:
            if len(set(element).intersection(numbers_map[4])) == 2:
                numbers_map[2] = set(element)
            elif len(set(element).intersection(numbers_map[1])) == 2:
                numbers_map[3] = set(element)
            else:
                numbers_map[5] = set(element)
        number_answer = []
        for number in numbers:
            for key, item in numbers_map.items():
                if set(number) == item:
                    number_answer += [key]
                    break
        final_sum += int(''.join(map(str,number_answer)))
    return final_sum

assert solve_part_one(open_data('test.txt')) == 26
assert solve_part_two(open_data('test.txt')) == 61229

print(solve_part_one(open_data('input.txt')))
print(solve_part_two(open_data('input.txt')))
