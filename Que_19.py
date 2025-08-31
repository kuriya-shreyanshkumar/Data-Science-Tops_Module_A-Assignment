"""19.Write a Python function that takes a list and returns a new list with unique
 elements of the first list."""
 
def unique_elements(input_list):
    unique_list = list(set(input_list))
    return unique_list