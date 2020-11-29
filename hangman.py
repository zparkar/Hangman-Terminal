# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:03:17 2020

@author: ZPARKAR2
"""

from random_words import RandomWords
from hangman import Hangman
import time
import pandas as pd
import json
from openpyxl import load_workbook
import datetime




input_flag=False
input_flag2=False
scores = {'name':[],'score':[]}
score_counter=0
games_played=1
print("Welcome to Hangman!")

while input_flag==False:
    
    play=input("Would you like to play? (yes to play or any key to quit): ")


    if play.lower()=="yes":
        print("Great! Starting Game....")
        time.sleep(2)
        name = input("Please enter your name: ")
        input_flag = True
        while input_flag2==False:
            game=Hangman()
            game.choose_difficuly()
            game.create_secret_word()
            game.format_secret_word()
            game.display_message()
            game.play_game()
            score_counter+=game.score
            play_again=input("Would you like to play again? (yes to play or any key to quit): ")
        
            if play_again.lower()=="yes":
                games_played+=1
                continue
            
            else:
                 scores['name'] = name.title()
                 scores['score'] = score_counter
                 scores['date'] = datetime.datetime.now()
                 scores['games played'] = games_played
                 try:
                     wb = load_workbook("hangman_scores.xlsx")
                     sheet = wb['Sheet1']
                     new_row = [f"{scores['name']}", f"{scores['score']}", f"{scores['date']}",games_played]    
                     sheet.append(new_row)
                     wb.save("hangman_scores.xlsx")
                 except:
                     score_data =pd.DataFrame(scores, index=[0])
                     score_data.to_excel("hangman_scores.xlsx",index=False)
                 df = pd.read_excel("hangman_scores.xlsx", header=0)
                 df = df.sort_values(by='score', ascending=False)
                 filtered_df = df.loc[df['name'] == name.title()]
                 max_score =filtered_df['score'].max()
                 df = df.reset_index(drop=True)
                 print(f"\nYour score: {score_counter}")
                 print(f"Your highest score: {max_score}")
                 print(f"Current Leader: {df['name'][0]}")
                 print(f"\nScoreboard\n{df}")
                 print("\nQuitting...")
                 time.sleep(2)
                 break

        
    else:
       print("Quitting...")
       time.sleep(2)
       break
    
