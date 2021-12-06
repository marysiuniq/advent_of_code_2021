# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 05:59:58 2021

@author: Marysia

Solution to puzzle from https://adventofcode.com/2021/day/6
"""

from copy import deepcopy

def open_data(in_name):
    '''
    Opens the data for the puzzle.
    '''
    with open(in_name, 'r') as file:
        out_data = file.readlines()
        out_data = out_data[0].split(',')
    return [int(x) for x in out_data]

def solve_part_one(in_list, in_days):
    '''
    Solves part one.
    '''
#    for day in range(in_days):
#        in_list = [_ - 1 for _ in in_list]
#        add_list = []
#        for pos, item in enumerate(in_list):
#           if item == -1:
#               in_list[pos] = 6
#               add_list.append(8)
#        if add_list:
#            in_list += add_list
#    return len(in_list)
    return solve_part_two(in_list, in_days)

def solve_part_two(in_list, in_days):
    '''
    Solves part two.
    '''
    regular_fish = list(range(1, 9))
    fish_dict = dict.fromkeys(range(9), 0)
    for fish in in_list:
        if fish in fish_dict.keys():
            fish_dict[fish] += 1
        else:
            fish_dict[fish] = 1
    for _ in range(in_days):
        dict_tmp = deepcopy(fish_dict)
        new_fish_num = 0
        additional_six = 0
        for fish in fish_dict:
            if fish_dict[fish]:
                if fish in regular_fish:
                    dict_tmp[fish-1] = fish_dict[fish]
                    dict_tmp[fish] = 0
                elif fish == 0:
                    dict_tmp[0] = 0
                    new_fish_num = fish_dict[0]
                    additional_six = fish_dict[0]
                else:
                    print('WTF?!')
        dict_tmp[8] = new_fish_num
        dict_tmp[6] += additional_six
        fish_dict = deepcopy(dict_tmp)
    return sum(fish_dict.values())

assert solve_part_one(open_data('test.txt'), 80) == 5934
assert solve_part_two(open_data('test.txt'), 256) == 26984457539

print(solve_part_one(open_data('input.txt'), 80))
print(solve_part_two(open_data('input.txt'), 256))
