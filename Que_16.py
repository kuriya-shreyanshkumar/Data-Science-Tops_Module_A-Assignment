"""16.Counting the frequencies in a list using a dictionary in Python. Input : [1, 1, 1, 5,
 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
 Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2
"""
num = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
frequency = {}
for n in num:
    if n in frequency:
        frequency[n] += 1
    else :
        frequency[n] = 1
print("frequency",frequency)            
