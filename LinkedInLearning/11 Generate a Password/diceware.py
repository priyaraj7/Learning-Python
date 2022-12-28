# # Python Code Challenge #11: Generate a Password

# Your goal is to implement a function, `generate_passphrase()`, that takes the number of words to include in the password as the input argument and returns a string containing a sequence of randomly selected words from the [Diceware list](https://theworld.com/~reinhold/diceware.wordlist.asc) separated by spaces.

# ```console
# >>> generate_passphrase(4)
# 'correct horse battery staple'
# ```










# import secrets

# def generate_passphrase(num_words, wordlist_path='diceware.wordlist.asc'):
#     with open(wordlist_path, 'r', encoding='utf-8') as file:
#         lines = file.readlines()[2:7778]
#         word_list = [line.split()[1] for line in lines]

#     words = [secrets.choice(word_list) for i in range(num_words)]
#     return ' '.join(words)


# # commands used in solution video for reference
# if __name__ == '__main__':
#     print(generate_passphrase(7))
#     print(generate_passphrase(7))