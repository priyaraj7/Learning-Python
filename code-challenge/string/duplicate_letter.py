"""
Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence. 
The function should return True if the sentence has any word with duplicate letters, else return False.
"""

def check_duplicate(string):
    # remove whitespace
    str1= string.replace(" ", "")
    # check length of set and input
    return len(set(str1)) < len(str1) 

print(check_duplicate("string")) # False
print(check_duplicate("string strujj jhjjb")) # True
print(check_duplicate("supriyaa")) # True