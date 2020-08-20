#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:49:47 2020

@author: elliotgross
"""

# Imports
import pandas as pd
import numpy as np

# Helper Methods
def add_current_votes_column(ballots_df):
    '''
    Add a 'current vote' column setting it equal to the 'first choice votes' column 

    Parameters
    ----------
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.

    Returns
    -------
    None.

    '''
    
    ballots_df.insert(loc=0, column='Current Votes', value=ballots_df[1])

def add_next_choice_column(ballots_df):
    '''
    Adds a 'next choice' column setting it equal to the 'second choice votes' column 

    Parameters
    ----------
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.

    Returns
    -------
    None.

    '''
    
    ballots_df.insert(loc=1, column='Next Choice', value=ballots_df[2])
    
 
def calculate_threshold(ballots_df, num_of_winners):
    '''
    This method calculates and returns the threshold. 
    
    The threshold is the number of votes over 1 plus than the number of winners,
    all floored, plus one.

    Parameters
    ----------
    ballots_df : pd.DataFrame
        A pandas dataframe of all the ballots.
    num_of_winners : int
        The amount of winners desired.

    Returns
    -------
    threshold : int
        The number of votes needed to be considered a 'winner'.

    '''
    
    threshold = int(np.floor((ballots_df.shape[0])/(num_of_winners+1))+1)
    return threshold
        
def remove_invalid_votes(ballots_df):
    
    '''
    This Method takes in a ballots dataframe and removes all the invalid votes.
    
    It checks the 'current votes' column and drops all the rows with NaN values in that
    column.

    Parameters
    ----------
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.

    Returns
    -------
    None.

    '''
    invalid_votes_index = list(ballots_df[ballots_df['Current Votes'].isna()==True].index)
    ballots_df.drop(invalid_votes_index, inplace=True)
    ballots_df.reset_index(drop=True, inplace=True)


def get_top_winner_above_threshold(ballots_df, threshold):
    '''
    This Method returns the canidate with the most current votes, while also being
    above the threshold. If no canidate is above the threshold, this method returns None.

    Parameters
    ----------
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.
    threshold : int
        The amount of votes needed to be considered a 'winner'.

    Returns
    -------
    top_winner_above_threshold : String
        The canidate with the most votes, also above the threshold.

    '''
    
    top_winner_above_threshold = None
    
    
    if ballots_df['Current Votes'].describe()['freq'] > threshold:
        top_winner_above_threshold = ballots_df['Current Votes'].describe()['top']
    
    return top_winner_above_threshold

def redistribute_votes(ballots_df, threshold, top_winner_above_threshold):
    '''
    This method redistributes the votes of the winner that  above the threshold,
    to the other canidates.
    
    This method first calculates the number of votes above the threshold and then gets
    the percentage of the exceeding votes compared to the total votes of the winner.
    The method then tallys up all the 'next choice' votes for the people that voted for the
    winner. Then, while looping through all the possible 'next choice canidates', the method
    obtains the previously mentioned percentage of the indeces of each next choice canidate.
    For each pair of indecies, the indecies are used to replace the values in the 'current
    votes' column with the respected canidate, at each index. 

    Parameters
    ----------
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.
    threshold : int
        The number of votes needed to be considered a 'winner'.
    top_winner_above_threshold : String
        The Canidate who's votes are being redistributed.

    Returns
    -------
    None.

    '''
    
    
    winners_votes = ballots_df[ballots_df['Current Votes']==top_winner_above_threshold]
    amount_of_winners_votes = winners_votes.shape[0]
    
    excess_votes = amount_of_winners_votes - threshold
    excess_votes_percent = np.round(excess_votes/amount_of_winners_votes,2)
    
    
    print(excess_votes, excess_votes_percent)
    
    
    total_votes_redistributed = 0
    for next_choice in winners_votes['Next Choice'].unique():
        
        amount_of_next_choice_votes = len(winners_votes[winners_votes['Next Choice']==next_choice].index)
        amount_of_votes_added = int(np.round(amount_of_next_choice_votes*excess_votes_percent))
        
        total_votes_redistributed += amount_of_votes_added
        
        
        print(amount_of_next_choice_votes*excess_votes_percent, amount_of_votes_added, total_votes_redistributed)
        #Problem - Votes dont amount to the total votes needed to be distributed
    
def eliminate_canidate(canidate, ballots_df):
    '''
    This method updates all the ballots and their ranks after removing the elminated
    canidate. 
    
    This method loops through all the columns, excluding the current_votes columns. Then, 
    for each column, it loops through all the rows, checking if the vote is for the 
    eliminated canidate. If it is, then a subset of the row is created, with the removed 
    vote and shifted values. Then the subset is rejoined with the beggining of the row,
    and then it replaces the orginial row. After finishing the loops, the dataframe is 
    updated.

    Parameters
    ----------
    canidate : String
        The canidate being eliminated.
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.

    Returns
    -------
    None.

    '''
    pass

def update_ballots_df(ballots_df):
    '''
    This method updates the ballots dataframe after removing the elimanted canidate.
    
    This method first calulates the canidate to be eliminated by finding the canidate with
    the least votes in the 'current votes' column. Then, the method
    'eliminate_canidate(canidate, ballots_df)' is called. This method updates
    all the votes and their ranks after removing the elminated canidate. 
    Then, the method updates the 'current votes' column. It does this by changing all the 
    values in the 'current votes' column that are equal to the eliminated canidate and 
    replacing the values with their next choice, which after being updated, are now in the 
    'first choice' column.

    Parameters
    ----------
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.

    Returns
    -------
    None.

    '''
    pass


# Wrapper Method
def main(ballots_df, num_of_winners):
    '''
    This method puts together all the helper methods and returns the total winners of the
    election.

    Parameters
    ----------
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.
    num_of_winners : int
        The number of winners in the election.

    Returns
    -------
    total_winners : list
        A list of all the winners.

    '''
    
    total_winners = []
    
    return total_winners