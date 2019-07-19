'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''

str_name = input("Please enter your name: ")
print("Your name in Pig Latin is:")
print( str_name[1:], str_name[0], "ay", sep='')
