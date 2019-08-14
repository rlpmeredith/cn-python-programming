'''
Using list comprehension, create a list that contains the individual
letters using the word "CodingNomads".

For example:

word = "CodingNomads"
..your code
result_list = ['C', 'o', 'd', 'i', 'n', 'g', 'N', 'o', 'm', 'a', 'd', 's']

'''
# Tested 14-08-19

result_list = []
word = "CodingNomads"
result_list = [letter for letter in word]
print(result_list)
