#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:00:57 2019

@author: hpitawela
"""

cases  = int(input())
for case in range(cases):
    n, Q = map(int, input().split())
    blocks = input()
    if n>1:
        main_dict = {}
        sub_dict = {}
        main_dict.update({0: sub_dict})
        for i in range(1,len(blocks)+1):
            dict_index = main_dict.get(i-1).copy()
            new_value = 1 if (dict_index.get(blocks[i-1]) == None) else dict_index.get(blocks[i-1])+1
            dict_index.update({blocks[i-1]: new_value})
            main_dict.update({i: dict_index})
        yes_count = 0

        for q in range(Q):
            l, r = map(int, input().split())
            low_dict = main_dict.get(l-1)
            high_dict = main_dict.get(r)
            odd_count = 0
            for high_key in high_dict.keys():
                low_val = 0 if low_dict.get(high_key) == None else low_dict.get(high_key)
                high_val = high_dict.get(high_key)
                if ((high_val - low_val)%2) == 1:
                    odd_count += 1
            if odd_count == 0 or odd_count == 1:
                yes_count += 1
    else:
        yes_count = 0
        for q in range(Q):
            input()
            yes_count += 1
    print('Case #{}: {}'.format(case + 1, yes_count), flush=True)
