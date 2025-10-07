"""19.Write a Python function that takes a list and returns a new list with unique
 elements of the first list."""
 
def unique_elements(input_list):
    unique_list = list(set(input_list))
    return unique_list

my_list = [1, 2, 2, 3, 4, 4, 5, 1]
result = unique_elements(my_list)

print("Original List:", my_list)
print("Unique Elements:", result)
