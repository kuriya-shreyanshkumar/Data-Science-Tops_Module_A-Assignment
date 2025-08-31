""" 17.Write a python program using function to find the sum of odd series and even
 series
 Odd series: 12/ 1! +32/ 3! + 52/ 5!+……n
 Even series: 22/ 2! + 42/ 4! + 62/ 6!+……n
"""
n = int(input("Enter the value of n: "))

# Odd series
odd_sum = 0
for i in range(1, n+1, 2):
	fact = 1
	for j in range(1, i+1):
		fact *= j
	term = (10*i + 2) / fact
	odd_sum += term
print("Sum of Odd Series:", odd_sum)

# Even series
even_sum = 0
for i in range(2, n+1, 2):
	fact = 1
	for j in range(1, i+1):
		fact *= j
	term = (10*i + 2) / fact
	even_sum += term
print("Sum of Even Series:", even_sum)


