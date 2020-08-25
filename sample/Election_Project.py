#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:49:47 2020

@author: elliotgross
"""


import pandas as pd
import numpy as np
import math


def undo_levels(df):
    '''
    This method strips the mutli-index and returns a dataframe with reseted indecies.

    Parameters
    ----------
    df : pd.DataFrame
        A dataframe of all the votes.

    Returns
    -------
    : pd.DataFrame
        A dataframe of all the votes, with reseted indecies.

    '''
    
    return df.reset_index().drop(['index','level_0'], axis=1, errors='ignore')

def eliminate_candidate(df, candidate):
    '''
    This method gets rid of all the instances of the inputed candidate and shifts 
    the next choice vote over. 

    Parameters
    ----------
    df : pd.DataFrame
        A dataframe of all the votes.
    candidate : String
        The candidate to be removed.

    Returns
    -------
    df : pd.DataFrame
        A dataframe with the inputed candidate removed

    '''
    df = undo_levels(df)
    

    for i,column in enumerate(df.columns.to_list()[:-1]):
        candidate_to_remove_index = df[df[column] == candidate].index
        
        #Shift from current column to final choice
        df.loc[candidate_to_remove_index,df.columns.to_list()[i:-1]] = df.loc[candidate_to_remove_index,
                                                                             df.columns.to_list()[:-1]].shift(-1,axis=1)
        
    # Re-Add Levels
    df = df.set_index(df.columns.to_list()[:-1]).sort_index()
    
    return df
    
def handle_winner(df, threshold, total_winners):
    '''
    This method finds the winner, calculates the new weight, distributes the votes using the new weight,
    and then removes the winner. Afterwards, the winner is added to the total_winners list. The df
    and total_winners are returned

    Parameters
    ----------
    df : pd.DataFrame
        A dataframe of all the votes.
    threshold : float
        The minimum amount of votes needed to secure a win.
    total_winners : list
        A list of the total winners.

    Returns
    -------
    df : pd.DataFrame
        A dataframe of all the votes, with the votes redistributed and the winner removed.
    total_winners : list
        A list of the winners of the election.

    '''
    
    top_winner_row = df.reset_index().groupby(['Choice 1']).sum().sort_values(['Weight'], ascending=False).iloc[0,:]
    
    winner_name, winner_votes = top_winner_row.name, top_winner_row['Weight']

    if winner_votes > threshold:
        new_weight = (winner_votes-threshold)/winner_votes
        
        df = undo_levels(df)
        
        #Redistribute Vote
        winner_rows_index = df[df['Choice 1'] == winner_name].index
        df.loc[winner_rows_index,'Weight'] *= new_weight
        
        #Get Rid of Winner
        df = eliminate_candidate(df, winner_name)

        total_winners.append(winner_name)
        
    return df, total_winners

def handle_loser(df):
    '''
    This method first calculates the loser and then removes them from the dataframe

    Parameters
    ----------
    df : pd.DataFrame
        A dataframe of all the votes.

    Returns
    -------
    df : pd.DataFrame
        A dataframe of all the votes with the loser removed.

    '''
    
def check_winner(df, threshold):
    '''
    This method first calculates the winner and returns the logistical outcome of the winner having
    more votes than the threshold.

    Parameters
    ----------
    df : pd.DataFrame
        A dataframe of all the votes.
    threshold : float
        The minimum amount of votes needed to secure a win.

    Returns
    -------
     : bool
        The outcome of the winner having more votes than the threshold.

    '''
    
    
def prepare_data(csv_filename, candidates):
    '''
    This method takes in a csv filename and the candidates and returns a multi-indexed,
    prepared dataframe.

    Parameters
    ----------
    csv_filename : String
        A filepath to the votes data.
    candidates : list
        A list of all the candidates.

    Returns
    -------
    df : pd.DataFrame
        A multi-indexed, prepared, dataframe.

    '''
    
def handle_invalid_votes(df):
    '''
    This method converts all NaN votes to 'Invalid' and then eliminates all the 'Invalid' votes
    with the eliminate_candidates(df, candidate) method.

    Parameters
    ----------
    df : pd.DataFrame
        A dataframe of all the votes.

    Returns
    -------
    df : pd.DataFrame
        A dataframe with invalid votes removed.

    '''

def run_rounds(df, num_of_winners, total_winners):
    '''
    This method retruns the total winners of the election.
    
    This method first checks if there are enough total winners. If there are, then the winners 
    are returned. If there aren't, the invalid votes are removed and then it checks for a winner. If
    there is a winner, then the handle_winner(df, threshold, total_winners) method is called and then 
    run_rounds(df, num_of_winners, threshold, total_winners) is called again. If there is no winner,
    then the handle_loser(df) method is called, followed by a recursive 
    run_rounds(df, num_of_winners, threshold, total_winners).
    
    Parameters
    ----------
    df : pd.DataFrame
        A dataframe of all the votes.
    num_of_winners : int
        The desired amount of winners.
    total_winners : list
        A list of the winners so far.

    Returns
    -------
    total_winners : list
        A list of the total winners.

    '''
    
    
    
def main(csv_filename, candidates, num_of_winners):
    '''
    This method first prepares the data, then runs the run_rounds(df, num_of_winners, total_winners)
    method and saves the total winners to a variable. The total_winners are then returned.

    Parameters
    ----------
    csv_filename : String
        A filepath to the votes data.
    candidates : list
        A list of all the candidates.
    num_of_winners : int
        The desired amount of winners.

    Returns
    -------
    total_winners : list
        The winners of the election.

    '''