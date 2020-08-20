#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:27:53 2020

@author: elliotgross
"""

import Election_Project as ep

import pandas as pd
import numpy as np

import copy

def generate_test(canidates, ballots, vote_spaces):
    ballots_dict = {}
    for i in range(1, vote_spaces+1):
        ballots_dict[i] = []
        
        
    for j in range(ballots):
        canidates_copy = copy.deepcopy(canidates)
        
        for i in range(1, vote_spaces+1):
            
            nth_choice = canidates_copy[np.random.randint(0, len(canidates_copy))]
            canidates_copy.remove(nth_choice)
            
            existing_choices = ballots_dict[i]
            existing_choices.append(nth_choice)
            
            ballots_dict[i] = existing_choices
        
        
    
    return pd.DataFrame(ballots_dict, columns=ballots_dict.keys())


canidates = ['Alan','Ben','Carlos','Dylan']
test_df = generate_test(canidates, 2000, 4)


#Tests

add_current_votes_column(test_df)
add_next_choice_column(test_df)

print(test_df)

threshold = calculate_threshold(test_df, 3)

remove_invalid_votes(test_df)

winner = get_top_winner_above_threshold(test_df, threshold)
print(winner)

redistribute_votes(test_df, threshold, winner)
