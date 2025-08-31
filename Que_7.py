# Program to find Greatest Common Divisor of two numbers. For example, the GCD of 20 and 28 is 4 and the GCD of 98 and 56 is 14.

num_1, num_2 = map(int, input("Enter two numbers separated by space: ").split())

while num_2:
    num_1, num_2 = num_2, num_1 % num_2
    
print(f"The Greatest Common Divisor (GCD) is: {num_1}")    
