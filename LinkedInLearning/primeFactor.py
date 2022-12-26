# # Python Code Challenge #1: Find Prime Factors

# Your goal is to implement a function, `get_prime_factors()`, that takes an integer value as the input argument and returns a list containing all of its prime factors.

# ## Example Test Output
# ```console
# >>> get_prime_factors(630)
# [2, 3, 3, 5, 7]
# ```

def get_prime_factors(integer):
    factorList = []
    divisor = 2

    while divisor <= integer:
        if integer % divisor == 0:
            factorList.append(divisor)
            integer = integer // divisor
        else:
            divisor += 1

    return factorList

print(get_prime_factors(630)) # [2, 3, 3, 5, 7]

print(get_prime_factors(10)) # [2, 5]

# Explanation

# 1.    factorList = [] 
# 2.    divisor = 2

# loop through the number till divisor is less or equal to input(integer)
#     1st Loop : 10 % 2 === 0 add to the list, input = 10 // 2 => 5
#     2nd loop: 5 % 2 != 0 else divisor = 3
#     3rd loop: 5 % 3 != 0 else divisor = 4
#     4th loop: 5 % 4 != 0 else divisor = 5
#     5th Loop : 5 % 2 == 0 add 5, to the list, input = 5 // 5 => 1
# exit loop because contition not met 

# return factorList = [5, 10] 
    




