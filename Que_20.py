"""20.Mini project :
 Problem Statement : Password Generator
 Make a program to generate a strong password using the input given by the user.
 To generate a password, randomly take some words from the user input and then
 include numbers, special characters and capital letters to generate the password.
 Also, keep a check that password length is more than 8 characters.
 Note: Include Exception handling wherever required. Also, make a ‘User’ class
 and store the details like user id, name and password of each user as a tuple.
"""
user_id = input("Enter User ID: ")
name = input("Enter Name: ")
user_input = input("Enter your password: ")


if not user_input.strip():
    raise ValueError("Input cannot be empty!")


word = user_input.split()[0]


password = word.capitalize() + "123" + "@#"


if len(password) <= 8:
    password = password + "XY"


binary_pass = ' '.join(format(ord(char), '08b') for char in password)


user_details = (user_id, name, binary_pass)


print("\nUser created successfully!\n")
print("User ID :", user_details[0])
print("Name    :", user_details[1])
print("Binary Password:", user_details[2])