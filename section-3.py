# Write a program to take as input a positive integer.
# The program is to output integers counting from 1 to the number input.
# For example, an input of 5 will output: 1 2 3 4 5

n = int(input('What is your positive integer? '))
for i in range(1,n+1):
    print(i)