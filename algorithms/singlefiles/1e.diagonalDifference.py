"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers
Return

int: the absolute diagonal difference
Input Format

The first line contains a single integer, , the number of rows and columns in the square matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
"""
number = 3
line1 = "11 2 4"
line2 = "4 5 6"
line3 = "10 8 -12"
first_diagonal = []
second_diagonal = []
# Convert to a 2D array

matrix = [list(map(int, line.split())) for line in [line1, line2, line3]]

for i in range(number):
    first_diagonal.append(matrix[i][i])
    second_diagonal.append(matrix[(number - 1) - i][i])

print(abs(sum(first_diagonal) - sum(second_diagonal)))
