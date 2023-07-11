#
# File: math-random.py
# Author: Mathew Kemp
# Email Id: Kemmy088
# Description: activity 2A- math and random
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

import random

number = random.randint(1,10)
print('please guess the random number (between 1-10): ')
guess = int(input())
print('random number is: ', number)
print('your guess was ', guess)
