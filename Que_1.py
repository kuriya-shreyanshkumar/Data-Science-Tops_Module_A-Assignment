# Write a python program to sum of the first n positive integers.

number  = int(input("Enter a positive integer: "))

if number < 1:
    print("Please enter a positive integer.")
else :
    sum_of_integers = sum(range(1, number + 1))
    print(f"The sum of the first {number} positive integers is: {sum_of_integers}")    

