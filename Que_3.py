# Write a Python program to count the occurrences of each word in a given sentence.

sentence = input("Enter a sentence: ")
words = sentence.split()
for i in set(words):
    print(f"'{i}' occurs {words.count(i)} times")