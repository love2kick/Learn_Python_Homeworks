a = "I am global variable!"


def enclosing_function():
    a = "I am variable from enclosed function!"

    def inner_function():

        # global a # : answer for 2.1
        nonlocal a # : answer for 2.2
        print(a)
    return inner_function()