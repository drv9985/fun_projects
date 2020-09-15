# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:47:24 2020

@author: Dhruv Mukherjee
"""

# Import libraries
import random

# functions
def guessing_game():
    user_input = int(input('Enter your number between 1 and 10: '))
    comp_generated = random.randint(1, 10)
    while True:
        if user_input == comp_generated:
            print('Your guess is right')
            break
        elif user_input > comp_generated:
            print('Your guess is higher than the actual number')
            user_input = int(input('Enter your number between 1 and 10: '))
        elif user_input < comp_generated:
            print('Your guess is lower than the actual number')
            user_input = int(input('Enter your number between 1 and 10: '))

# call function
guessing_game()