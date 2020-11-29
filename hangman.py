# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:43:13 2020

@author: ZPARKAR2
"""

from random_words import RandomWords

class Hangman:
    
    def __init__(self,difficulty=1,tries=6):
        self.difficulty=difficulty
        self.tries=tries
        self.secret_word=[]
        self.picked_word=""
        self.guessed_letters=[]
        self.guessed_correct=0
        self.guessed_incorrect=0
        self.guessed_word=""
        self.options=['Normal','Hard (score is doubled)', 'Hardest (score is tripled!)']
        self.hangman_pics= ['''
                         +---+
                             |
                             |
                             |
                        ===''', '''
                         +---+
                         O   |
                             |
                             |
                        ===''', '''
                         +---+
                         O   |
                         |   |
                             |
                        ===''', '''
                         +---+
                         O   |
                        /|   |
                             |
                        ===''', '''
                         +---+
                         O   |
                        /|\  |
                             |
                        ===''', '''
                         +---+
                         O   |
                        /|\  |
                        /    |
                        ===''', '''
                         +---+
                         O   |
                        /|\  |
                        / \  |
                        ===''']
        self.wins=0
        self.score=0
    
    def choose_difficuly(self):
        print("\nPlease choose Difficulty:")
        for idx, element in enumerate(self.options):
            print("{}) {}".format(idx+1,element))
        while True:
            i = input("Enter number: ")
            print(i)
            if i.isdigit()==False or int(i) <0 or int(i) > len(self.options):
             print("Please enter a valid number!")
             continue
            else:
                self.difficulty=int(i)
                self.tries=int(self.tries/self.difficulty)
                break

    
    def create_secret_word(self):
        rw=RandomWords()
        self.picked_word=rw.random_word().upper()
        return self.picked_word
    
    def format_secret_word(self):
        for i in self.picked_word:
            self.secret_word.append(i)
        return self.secret_word
    
    def display_message(self):
        self.guessed_word= ["_"] * len(self.secret_word)
        print("\nGuess the following word: \n")
        print(*self.guessed_word, sep=' ')
        
    def play_game(self):
        while self.tries>0:
            self.guess_letter=input("Input a letter: \r")    
            if self.guess_letter.upper() in self.guessed_letters:
                print("You already used that letter!")
    
     
            elif self.guess_letter.upper() in self.secret_word:
                 self.guessed_letters.append(self.guess_letter.upper())
                 for i in range(self.secret_word.count(self.guess_letter.upper())):
                     index_letter=self.secret_word.index(self.guess_letter.upper())
                     self.guessed_word[index_letter]=self.guess_letter.upper()
                     self.guessed_correct+=1
                     self.secret_word[index_letter]="-"
                 print(*self.guessed_word, sep=' ')

         
                 if self.guessed_correct==len((self.secret_word)):
                     print(self.picked_word)
                     print("\nCongratulations! You won!")
                     self.wins+=1
                     self.scoreboard()
                     break
         
                 else:
                    continue     
            else:
                self.tries-=1
                self.guessed_incorrect+=self.difficulty
                self.guessed_letters.append(self.guess_letter.upper())
                print(f"Incorrect. You have {self.tries} tries left ")
                print(self.hangman_pics[self.guessed_incorrect])
                print(*self.guessed_word, sep=' ')
                continue
     
        if self.tries==0:
            print(f"\nGame over! The word was '{self.picked_word}'. ")
            
    def scoreboard(self):
        self.score = int(self.difficulty * len(self.secret_word) * self.wins)

        
        
    
            
    
    
