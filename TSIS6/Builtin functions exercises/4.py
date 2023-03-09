"""Write a Python program that invoke square root function after specific milliseconds.
Sample Input:
25100
2123
Sample Output:
Square root of 25100 after 2123 miliseconds is 158.42979517754858"""
import time
import math

number = int(input("Enter a number: "))


delay = int(input("Milliseconds: "))

delay /= 1000

time.sleep(delay)

result = math.sqrt(number)

print(f"Square root of {number} after {delay*1000} milliseconds is {result}")
