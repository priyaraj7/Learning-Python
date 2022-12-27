# # Python Code Challenge #9: Simulate Dice

# Your goal is to implement a function, `roll_dice()`, 
# that takes a variable number of input arguments representing the number of sides 
# on an arbitrary number of dice, its and its output should print a table of the 
# probability for each possible outcome.

# ## Example Test Output
# Rolling one four-sided die and two six-sided dices:
# ```console
# >>> roll_dice(4,6,6)

# OUTCOME PROBABILITY
# 3       0.69%
# 4       2.06%
# 5       4.14%
# 6       6.95%
# 7       9.70%
# 8       12.55%
# 9       13.93%
# 10      13.85%
# 11      12.52%
# 12      9.70%
# 13      6.95%
# 14      4.17%
# 15      2.09%
# 16      0.70%
# ```


import random
from collections import Counter

def roll_dice(*dice, num_trials = 1_000_000):
    counts = Counter()
    for _ in range(num_trials):
        counts[sum((random.randint(1, sides) for sides in dice))] += 1

    print('\nOUTCOME\tPROBABILITY')
    for outcome in range(len(dice), sum(dice) +1):
        print(f'{outcome}\t{counts[outcome]* 100/ num_trials :0.2f}%')

roll_dice(4, 6, 6)
roll_dice(4, 6, 6, 20)
