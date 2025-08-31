#14.Write a Python program to find the highest 3 values in a dictionary

data = {'a': 5, 'b': 1, 'c': 3, 'd': 7, 'e': 2}
top_3 = sorted(data.values(), reverse=True)[:3]
print("Top 3 highest values:", top_3)