'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
# Stuck
input_dict = {"item1": 5, "item2": 6, "item3": 1}
highest = 0
result_list = []
temp_tuple = ()
for i in input_dict:
    for j in input_dict:
        if input_dict[j] >= highest:
            temp_tuple = (j, input_dict[j])
            result_list.append(temp_tuple)
            highest = input_dict[j]
print(result_list)
