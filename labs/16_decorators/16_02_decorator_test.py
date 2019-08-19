def decorator_func(initial_func):
    def wrapper_func():
        print("wrapper function picked some...")
        return initial_func()
    return wrapper_func

def prettify():
    print("flowers for you")

decorated_pretty = decorator_func(prettify)

decorated_pretty()