# assert is a built-in keyword in Python
# there will only be output if there is an assertion error

# this is how you define a function in python:
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
    # assert sum([1, 1, 1]) == 6, "Should be 6"
# note that [1, 2, 3] is called a "list" in python, rather than "array"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
# (1, 2, 2) is called a "tuple"

# this is how you define an "if" statement. The following conditional defines the files' entry point, meaning that when you run the file on the command line it will call the functions inside the statement:
if __name__ == "__main__":
    # you call a function just like in JS
    test_sum() 
    test_sum_tuple()
    # the following function wont be called given that an assertion error will be detected as a result of the previous function call
    print("Everything passed")
