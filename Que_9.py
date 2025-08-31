# Write a Python program to find the second smallest number in a list.
numbers = [34, 1, 23, 4, 3, 12, 45, 2, 5]
unique_numbers = list(set(numbers))   
unique_numbers.sort()
if len(unique_numbers) < 2:
    print("There is no second smallest number.")
else:
    print("The second smallest number is:", unique_numbers[1])