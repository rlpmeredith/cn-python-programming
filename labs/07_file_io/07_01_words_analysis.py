'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
# Tested 07-08-2019

words = []
shortest = 999
longest = 0
shortlist = []
longlist = []

with open('words.txt', 'r') as fin:
    for line in fin.readlines():
        line = line.rstrip()
        words.append(line)

for word in words:
    if len(word) < shortest:
        shortest = len(word)
        shortlist = [word]
    elif len(word) == shortest:
        shortlist.append(word)

print(shortlist)

for word in words:
    if len(word) > longest:
        longest = len(word)
        longlist = [word]
    elif len(word) == longest:
        longlist.append(word)

print(longlist)

print(len(words))
