"""
Given an array of integers, find the sum of its elements.

For example, if the array , , so return .

Function Description

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.

Constraints


Output Format

Print the sum of the array's elements as a single integer.
"""

arrayLength = 6
arrayNumbers = "1 2 3 4 10 11"

# Split the string into a list of strings
number_strings = arrayNumbers.split()

# Convert the list of strings to a list of integers
numbers_array = list(map(int, number_strings))
returnSum = 0

for number in numbers_array:
    returnSum = returnSum + number

print(returnSum)
