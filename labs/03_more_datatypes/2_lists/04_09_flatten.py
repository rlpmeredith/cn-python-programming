'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

#starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
#flat_list=[]
#for sublist in starting_list:
#    for item in sublist:
#        flat_list.append(item)
#print(flat_list)


starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flat_list=[]
flat_list = sum(starting_list, [])
print(flat_list)


