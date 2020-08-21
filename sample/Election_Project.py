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
def add_weights_to_dataframe(ballots_df):
    '''
    Adds weights to each value in the dataframe.

    Parameters
    ----------
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.

    Returns
    -------
    None.

    '''
    
    for column in ballots_df.columns:
        for i,value in enumerate(ballots_df[column]):
            if column == 1:
                ballots_df.loc[i, column] = (value, 1)
            else:
                ballots_df.loc[i, column] = (value, 0) 
    

def get_tallied_votes(canidates, ballots_df):
    '''
    Adds weights to each value in the dataframe.

    Parameters
    ----------
    canidates : list
    A list of canidates.
    
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.

    Returns
    -------
    tallied_votes : dictionary
        A dictionary of each canidate and their total votes.

    '''
    
    tallied_votes = {}
    for canidate in canidates:
        tallied_votes[canidate] = 0
        
    for column in ['Current Votes', 'Next Choice']:
        for i,value in enumerate(ballots_df[column]):
            tallied_votes[value[0][0]] += value[1]
    
    for key in tallied_votes.keys():
        tallied_votes[key] = np.round(tallied_votes[key])
        
    return tallied_votes
    
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


def get_top_winner_above_threshold(ballots_df, threshold, canidates):
    '''
    This Method returns the canidate with the most current votes, while also being
    above the threshold. If no canidate is above the threshold, this method returns None.

    Parameters
    ----------
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.
    threshold : int
        The amount of votes needed to be considered a 'winner'.
    canidates : list
        A list of all the canidates.

    Returns
    -------
    top_winner_above_threshold : String
        The canidate with the most votes, also above the threshold.

    '''
    
    top_winner_above_threshold = None
    
    
    tallied_votes = get_tallied_votes(canidates, ballots_df)
    
    most_votes = 0
    for key in tallied_votes.keys():
        if tallied_votes[key] > threshold:
            if tallied_votes[key] > most_votes:
                top_winner_above_threshold = key
                most_votes = tallied_votes[key]
                
    return top_winner_above_threshold

def redistribute_votes(ballots_df, threshold, top_winner_above_threshold, canidates):
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
    canidates : list
        A list of all the canidates.
        
    Returns
    -------
    ballots_df : pd.DataFrame
        A list of all the ballots.

    '''
    
    winners_votes = ballots_df[ballots_df['Current Votes'].apply(lambda x: x[0][0]) == top_winner_above_threshold]

    tallied_votes = get_tallied_votes(canidates, ballots_df)
    amount_of_winner_votes = tallied_votes[top_winner_above_threshold]
    
    excess_votes = amount_of_winner_votes - threshold
    excess_votes_percentage = np.round(excess_votes/amount_of_winner_votes,3)
    
    print(excess_votes, excess_votes_percentage)
    
    winners_votes['Current Votes'] = winners_votes['Current Votes'].apply(lambda x: (x[0],x[1]-excess_votes_percentage))
    winners_votes['Next Choice'] = winners_votes['Next Choice'].apply(lambda x: (x[0],x[1]+excess_votes_percentage))
    
    ballots_df.loc[winners_votes.index] = winners_votes
    
    
    return ballots_df

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
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.

    '''
    
       
    losers_votes = ballots_df[ballots_df['Current Votes'].apply(lambda x: x[0][0]) == canidate]
    previous_weights = [i for i in losers_votes['Current Votes'].apply(lambda x: x[1])]


    losers_votes['Current Votes'] = [(losers_votes['Next Choice'].apply(lambda x: (x[0][0],x[0][1])).iloc[i],
            losers_votes['Current Votes'].apply(lambda x: x[1]).iloc[i]) for i in range(len(losers_votes['Current Votes'].apply(lambda x: x[1])))]

    for i,value in enumerate(losers_votes['Next Choice']):
        i = losers_votes.index[i]
        
        next_rank = value[0][1]+1
        next_choice_canidate = losers_votes.loc[i, next_rank][0][0]
        while next_choice_canidate == np.nan:
            next_rank += 1
            next_choice_canidate = losers_votes.loc[i, next_rank][0][0]

        losers_votes.loc[i, 'Next Choice'] = ((next_choice_canidate, next_rank),
                                              losers_votes.loc[i, 'Next Choice'][1])
           
    losers_next_votes = ballots_df[ballots_df['Next Choice'].apply(lambda x: x[0][0]) == canidate]
    
    for column in ballots_df.columns:
        for i,value in enumerate(ballots_df[column]):
            if value[0][0] == canidate:
                ballots_df.loc[i,column] = ((np.nan, column),value[1])
                
                
    for i,value in enumerate(losers_next_votes['Next Choice']):
        i = losers_next_votes.index[i]
        
        next_rank = value[0][1]+1
        next_choice_canidate = losers_next_votes.loc[i, next_rank][0][0]
        while next_choice_canidate == np.nan:
            next_rank += 1
            next_choice_canidate = losers_next_votes.loc[i, next_rank][0][0]

        losers_next_votes.loc[i, 'Next Choice'] = ((next_choice_canidate, next_rank),
                                              losers_next_votes.loc[i, 'Next Choice'][1])
                
    
    ballots_df.loc[losers_votes.index] = losers_votes
    ballots_df.loc[losers_next_votes.index] = losers_next_votes
    return ballots_df
    

def update_ballots_df(ballots_df, canidates):
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
    canidates : list
        A list of all the canidates.
        
    Returns
    -------
    ballots_df : pd.DataFrame
        A dataframe of all the ballots.

    '''
    
    tallied_votes = get_tallied_votes(canidates, ballots_df)
    
    loser = None
    least_votes = 9999999
    for key in tallied_votes.keys():
        if tallied_votes[key] < least_votes:
            loser = key
            least_votes = tallied_votes[key]
            
    canidates.remove(loser)
    ballots_df = eliminate_canidate(loser, ballots_df)
    
    print(loser)
    return ballots_df
    
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