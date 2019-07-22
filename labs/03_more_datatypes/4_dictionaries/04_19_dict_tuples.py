'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''
# Tested 22-07-19. Same mess as before............

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = []
lowest_value = 999
my_key = ""
for i in range(0, len(input_dict)):
    for j in input_dict:
        if input_dict[j] < lowest_value:
            my_key = j
            lowest_value = input_dict[j]
            my_tuple = (my_key, lowest_value)
    result_list.append(my_tuple)
    input_dict.pop(my_key)
    lowest_value = 999
print(result_list)
