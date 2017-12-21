WINNING_CASES = [1 ,3, 2]
WINNING_CASES_EXPLANATION = ["BIG PRIZE", "Last 5 Digits", "Amorti"]
NUM_DIGITS = [7, 5, 1]
MAX_DIGITS = NUM_DIGITS

from random import *

BIG_PRIZE = []
for i in range (1,8):
    randnumber = randint(0,10)
    BIG_PRIZE.append(randnumber)

print BIG_PRIZE
