# Write a program to take as input air temperature in degrees Celsius.
# The program is to output a message to say whether it is freezing (below 1 degree) or not.
print('Running Program 1')
tempC = int(input('What is the temperature in celcius? '))
if tempC < 1:
    print('This is freezing!')
else:
    print('This is not freezing.')

# * Amend your program from (3) to say whether the water in a container is frozen, liquid or boiling.
print('Running Program 2')
tempC = int(input('What is the temperature in celcius? '))
if tempC >= 100:
    print('This is boiling!')
elif tempC >= 1:
    print('This is liquid')
else:
    print('This is frozen')



# Write a program to take as input an integer between 1 and 12 (inclusive).
# The program is to output the name of the month corresponding to the number input.
# For example, an input of 2 will output ‘February’. Hint: use a CASE statement.
print('Running Program 3')
month_num = int(input('Month #: '))
month_dict = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

print('That is ', month_dict[month_num])