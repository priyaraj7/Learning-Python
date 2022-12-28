# # Python Code Challenge #10: Count Unique Words

# Your goal is to implement a function, `count_words()`, 
# that takes the path to a text file as the input argument 
# and prints the total number of words in the file, as well as the top 20 most f
# requently used words and how many times each of them occurs.

# ## Example Test Output
# Using [The Complete Works of William Shakespeare](https://www.gutenberg.org/cache/epub/100/pg100.txt) as input:

# ```console
# >>> count_words('shakespeare.txt')


# Total Words: 976836

# Top 20 Words:
# THE      30257
# AND      28413
# I        23070
# TO       20997
# OF       18824
# A        16163
# YOU      14570
# MY       13179
# IN       12333
# THAT     12063
# IS       9858
# NOT      9066
# WITH     8531
# ME       8262
# FOR      8244
# IT       8212
# HIS      7583
# BE       7384
# THIS     7165
# HE       7100
# ```

import re
import collections

def count_words(path):
     with open(path, 'r') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
         #print(all_words) # gives list of all words in uppercase
        print(f'\nTotal Words: {len(all_words)}')

        word_counts = collections.Counter(all_words)
         # print(word_counts) # {'THE': 48, 'OF': 30, 'S': 13, 'AND': 12, 'THY': 12,.....} word count in key value pair

        print('\nTop 20 words:')
        for word in word_counts.most_common(15):
            print(f'{word[0]}\t{word[1]}')




count_words('LinkedInLearning/10 Count Unique Words/shakespear.txt') 