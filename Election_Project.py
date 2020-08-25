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

def eliminate_canidate(df, canidate):
    '''
    This method gets rid of all the instances of the inputed canidate and shifts the next choice vote 
    over. 

    Parameters
    ----------
    df : pd.DataFrame
        A dataframe of all the votes.
    canidate : String
        The canidate to be removed.

    Returns
    -------
    df : pd.DataFrame
        A dataframe with the inputed canidate removed

    '''
    
    
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
    
    
def prepare_data(csv_filename, canidates):
    '''
    This method takes in a csv filename and the canidates and returns a multi-indexed,
    prepared dataframe.

    Parameters
    ----------
    csv_filename : String
        A filepath to the votes data.
    canidates : list
        A list of all the canidates.

    Returns
    -------
    df : pd.DataFrame
        A multi-indexed, prepared, dataframe.

    '''
    
def handle_invalid_votes(df):
    '''
    This method converts all NaN votes to 'Invalid' and then eliminates all the 'Invalid' votes
    with the eliminate_canidates(df, canidate) method.

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
    
    
    
def main(csv_filename, canidates, num_of_winners):
    '''
    This method first prepares the data, then runs the run_rounds(df, num_of_winners, total_winners)
    method and saves the total winners to a variable. The total_winners are then returned.

    Parameters
    ----------
    csv_filename : String
        A filepath to the votes data.
    canidates : list
        A list of all the canidates.
    num_of_winners : int
        The desired amount of winners.

    Returns
    -------
    total_winners : list
        The winners of the election.

    '''