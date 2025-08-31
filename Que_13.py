#  13.Write a Python program to sort a dictionary (ascending /descending) by value.

sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))

print("Sorted Dictionary (Ascending):", sorted_asc)
print("Sorted Dictionary (Descending):", sorted_desc)
