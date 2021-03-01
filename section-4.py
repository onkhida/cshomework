# Write a program that asks the user for an integer between 1 and 5 (inclusive).
# The program is to check that the input is within the range and if not, prompt the user for a valid integer until the input is within the range.

n = 0
while n < 1 or n > 5:
    n = int(input('Enter a number between 1 and 5 inclusive '))

