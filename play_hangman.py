# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:03:17 2020

@author: ZPARKAR2
"""

from random_words import RandomWords
from hangman import Hangman
import time


input_flag=False
input_flag2=False

print("Welcome to Hangman!")

while input_flag==False:

    play=input("Would you like to play? (yes to play or any key to quit): ")


    if play.lower()=="yes":
        print("Great! Starting Game....")
        time.sleep(2)
        input_flag = True
        while input_flag2==False:
            game=Hangman()
            game.choose_difficuly()
            game.create_secret_word()
            game.format_secret_word()
            game.display_message()
            game.play_game()
            
            play_again=input("Would you like to play again? (yes to play or any key to quit): ")
        
            if play_again.lower()=="yes":
                continue
            
            else:
                 print("Quitting...")
                 time.sleep(2)
                 break

        
    else:
       print("Quitting...")
       time.sleep(2)
       break
    