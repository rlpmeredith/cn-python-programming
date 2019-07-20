'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
# tested 19-07-19
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = list()
for i in list_:
    count_ = 0
    for j in list_:
        if j == i:
            count_ += 1
    if count_ == 1:
        unique_list.append(i)
print(unique_list)

