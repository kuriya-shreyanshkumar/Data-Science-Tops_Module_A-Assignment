# Write a Python program to count occurrences of a substring in a string.

main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

count = main_string.count(substring)
print(f"The substring '{substring}' occurs {count} times in the main string.")

