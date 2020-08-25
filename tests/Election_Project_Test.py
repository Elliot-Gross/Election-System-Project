#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:50:46 2020

@author: elliotgross
"""


import Election_Project





canidates = ["A", "B", "C"]
csv_filename = "test_data.csv"
num_of_winners = 2

winners = main(csv_filename, canidates, num_of_winners)
winners



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
test_df = generate_test(canidates, 200, 4)
test_df = test_df.reset_index(drop=True)
test_df


canidates = ['Alan','Ben','Carlos','Dylan']
csv_file_name = "test2_df.csv"
num_of_winners = 1

winners = main(csv_file_name, canidates, num_of_winners)
winners