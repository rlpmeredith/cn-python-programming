'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
#Tested 06-08-19

newlist = []
reverselist = []

with open('words.txt', 'r') as fin:
    for w in fin.readlines():
        w = w.rstrip()
        newlist.append(w)

for w in reversed(newlist):
    reverselist.append(w)

with open('words_reverse.txt', 'w') as fout:
    fout.write("\n".join(reverselist))







