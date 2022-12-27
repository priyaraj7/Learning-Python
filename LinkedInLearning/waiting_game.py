# # Python Code Challenge #5: Play the Waiting Game

# Your goal is to implement a function, `waiting_game()`, that prints a message for the player to wait a random amount of time, somewhere between two to four seconds. When the player presses Enter, that starts a timer. The player's goal is to wait the specified number of seconds and then press Enter again. That displays the elapsed time, along with a message about whether the player was too fast, too slow, or right on target. 

# ## Example Test Output
# ```console
# >>> waiting_game()

# Your target time is 2 seconds
#  ---Press Enter to Begin---

# ...Press Enter again after 2 seconds...

# Elapsed time: 1.680 seconds
# (0.320 seconds too fast)
# ```

import time
import random

def waiting_game():
    target = random.randint(2,4) # target second tp wait
    print(f'\nYour target time is {target} seconds')

    input(' ---Press Enter to Begin--- ')
    start = time.perf_counter() # returns the float value of time in seconds.

    input(f'\n... Press Enter agin after {target} seconds...')
    elapsed = time.perf_counter() - start

    print(f'\nElapsed time: {elapsed :3f} seconds')
    if elapsed == target:
        print('Unbelievable! Perfect timing!')
    elif elapsed < target:
        print(f'({target - elapsed :.3f} seconds too fast)')
    else:
        print(f'({elapsed  - target :.3f} seconds too slow)')

waiting_game()






















