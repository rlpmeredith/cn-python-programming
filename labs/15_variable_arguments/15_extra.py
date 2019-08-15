def my_function(**kwargs):
    for i, j in kwargs.items():
        print(f"{i} {j}")


my_function(item1='hi', item2='hello')