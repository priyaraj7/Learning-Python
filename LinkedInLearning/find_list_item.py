# # Python Code Challenge #4: Find All List Items

# Your goal is to implement a function, `index_all()`, that takes a list of objects 
# and the item to search for as input arguments and returns a list of indices for where that item exists within the list.

# NOTE: Since the input argument could be a list of lists, your function should be able to traverse multidimensional 
# lists to find all instances of the item, and the elements of the returned list should also be lists to indicate multidimensional indices.

# ## Example Test Output
# ```console
# >>> example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
# >>> index_all(example, 2)
# [[0, 0, 1], [0, 1], [1, 1]]
# >>> print(index_all(example, [1, 2, 3]))
# [[0, 0], [1]]
# ```

# The enumerate() method adds a counter to an iterable and returns it (the enumerate object).

# languages = ['Python', 'Java', 'JavaScript']

# enumerate_prime = enumerate(languages)

# # convert enumerate object to list
# print(list(enumerate_prime))

# # Output: [(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]


def index_all(search_list, item):
    index_list = []
    for index, value in enumerate(search_list):
        # print(index, value)
        if value == item:
            index_list.append([index])
        # check if numbers is instance of list
        elif isinstance(search_list[index], list):
            # recursively call index_all function
            for i in index_all(search_list[index], item):
                # print(i, "i") 
                index_list.append([index] + i)
    return index_list





example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
print(index_all(example, 2)) # [[0, 0, 1], [0, 1], [1, 1]]
print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]










# def index_all(search_list, item):
#     index_list = []
#     for index, value in enumerate(search_list):
#         if value == item:
#             index_list.append([index])
#         elif isinstance(search_list[index], list):
#             for i in index_all(search_list[index], item):
#                 index_list.append([index] + i)
#     return index_list


# # commands used in solution video for reference
# if __name__ == '__main__':
#     example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
#     print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
#     print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]