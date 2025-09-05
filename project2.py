import math

# A Python program to calculate the area and perimeter of a rhombus.

# The formulas used are:
# Area (A) = (d1 * d2) / 2, where d1 and d2 are the lengths of the diagonals.
# Perimeter (P) = 4 * a, where 'a' is the length of one side.

# --- Example 1: Calculating Area ---
# Define the lengths of the two diagonals.
diagonal1 = 12.0
diagonal2 = 16.0

# Calculate the area of the rhombus.
area = (diagonal1 * diagonal2) / 2

# Print the result for the area calculation.
print("--- Area Calculation ---")
print(f"For a rhombus with diagonals of {diagonal1} and {diagonal2}:")
print(f"The area is: {area:.2f}\n")

# --- Example 2: Calculating Perimeter ---
# To find the perimeter, we need the length of one side.
# If we only have the diagonals, we can find the side length
# using the Pythagorean theorem on one of the four right triangles
# formed by the intersecting diagonals.
# The sides of the triangle are half of each diagonal.
side_a = diagonal1 / 2
side_b = diagonal2 / 2

# The side of the rhombus is the hypotenuse (c) of the triangle.
# a^2 + b^2 = c^2  => c = sqrt(a^2 + b^2)
side_length = math.sqrt(side_a**2 + side_b**2)

# Now, calculate the perimeter of the rhombus.
perimeter = 4 * side_length

# Print the result for the perimeter calculation.
print("--- Perimeter Calculation ---")
print(f"With diagonals of {diagonal1} and {diagonal2}, the side length is: {side_length:.2f}")
print(f"The perimeter is: {perimeter:.2f}")

# Note: The ':.2f' formatting is used to round the results to two decimal places.
