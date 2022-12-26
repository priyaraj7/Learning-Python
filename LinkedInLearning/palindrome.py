# # Python Code Challenge #2: Identify a Palindrome

# Your goal is to implement a function, `is_palindrome()`, that takes a text string as the input argument and returns a boolean indicating whether or not it's a palindrome.

# ## Example Test Output
# ```console
# >>> is_palindrome('hello world')
# False
# >>> is_palindrome('Go hang a salami, I’m a lasagna hog.')
# True
# ```

# Explanation : 2 pointer approach
# input:MAD AM
# output: True

# first remove all special character and white Space 
# convert it into lower case
 
#  create variable called firstindex = 0 and lastindex = length -1

#  loopthrough the input => till condition True
  
#   if first and last character are not same return False
#   else increment the firstindex and decrement the last Index  

# return true

def is_palindrome(input_str):
    # Using filter and isalnum to remove special characters
    # Converting the iterable to string using the join method
    # conver it into lowercase
    normal_string = "".join(filter(str.isalnum, input_str)).lower()
   
    head = 0
    tail = len(normal_string) - 1
    # loop through
    while head <= tail:
        if normal_string[head] != normal_string[tail]:
            return False 
        else:
            head = head + 1
            tail = tail -1
    # return result
    return True

print(is_palindrome('hello world'))
print(is_palindrome('Go hang a salami, I’m a lasagna hog.'))

print("world"[:: -1]) # dlrow


# SOLUTION FROM LINKDIN
import re

def is_palindrome1(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards

print(is_palindrome1('hello world'))
