#11.Write a Python program to unzip a list of tuples into individual lists.

list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]


unzipped = list(zip(*list_of_tuples))


list1, list2 = map(list, unzipped)  

print("List 1:", list1)
print("List 2:", list2)