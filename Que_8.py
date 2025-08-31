# Write a Python program to check whether a list contains a sublist.

main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = [4, 5, 6]

if str(sub_list)[1:-1] in str(main_list):
    print("The main list contains the sublist.")
else:
    print("The main list does not contain the sublist.")    