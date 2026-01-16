"""
2 Write a program that calculates the length of the hypotenuse in a right-angled triangle. The user needs to input the lengths of the two shorter sides.
Tip 1: Ask an AI about the formula for the Pythagorean theorem if you need it, but be careful not to ask for code that solves the task! Ask: “Briefly explain how the formula for the Pythagorean theorem works.”
Tip 2: Calculate the square root using math.sqrt().

As test data (to check if your program calculates correctly), you can use a triangle with sides 3, 4, and 5.
"""

import math

side_a = float(input("Enter the length of the first side: "))
side_b = float(input("Enter the length of the second side: "))

hypotenuse = math.sqrt(side_a**2 + side_b**2)

print("The length of the hypotenuse is:", hypotenuse)
