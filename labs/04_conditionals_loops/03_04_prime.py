'''
Print out every prime number between 1 and 100.

'''
# Logic could be improved but works! 23-07-19
#for my_num in range(2, 101):
#    for i in range(2, 101):
#        if (my_num % i) == 0 and (my_num / i) == 1:
#                print(my_num)
#                break
#        if (my_num % i) == 0:
#            break

for my_num in range(2, 101):
    for i in range(2, 101):
        if (my_num % i) == 0:
            if (my_num / i) == 1:
                print(my_num)
            break
