# # Python Code Challenge #6: Save a Dictionary

# Your goal is to implement two functions, `save_dict()` and `load_dict()`. 
# The `save_dict()` function takes two inputs arguments for the dictionary to save and an output file path. 
# The `load_dict()` function takes an input argument of the file path to the saved dictionary and returns its stored dictionary object.

# ## Example Test Output
# ```console
# >>> save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pickle')
# print(load_dict('test.pickle'))
# {1: 'a', 2: 'b', 3: 'c'}
# ```

# https://rizdelhi.medium.com/how-to-save-a-dictionary-to-a-file-in-python-6e5c17b0a1cc
# https://www.bogotobogo.com/python/python-json-dumps-loads-file-read-write.php

#   1st method using pickle
import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)

def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


# commands used in solution video for reference
if __name__ == '__main__':
    test_dict = {1: 'a', 2: 'b', 3: 'c'}
    save_dict(test_dict, 'test_dict.pickle')
    recovered = load_dict('test_dict.pickle')
    print(recovered)  # {1: 'a', 2: 'b', 3: 'c'}

#  2nd method using JSON

import json

def save_dict(dict_to_save, file_path):
    with open(file_path, "w") as t:
        json.dump(dict_to_save, t, indent = 2 )

def load_dict(file_path):
    with open(file_path, "rb") as t:
        return json.load(t)

test_dict = {1: 'a', 2: 'b', 3: 'c'}
save_dict(test_dict, 'test_dict.json')
recovered = load_dict('test_dict.json')
print(recovered)  # {1: 'a', 2: 'b', 3: 'c'}


