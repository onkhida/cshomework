# Write a program to take as input the length and width of a rectangular garden.
# The program is to calculate and output the surface area.
# solution to problem one

print('Running Program 1!')
length = input('What is the length of the rectangle? ')
width = input('What is the width of the rectangle? ')

print('The surface area is {}'.format(int(length) * int(width)))

# Write a program to take as input a temperature in degrees Fahrenheit.
# The program is to convert and output the temperature in degrees Celsius (Hint: DegreesC = (DegreesF – 32) * 5/9)
print('')
print('Running Program 2!')
temp_F = input('What is the temperature in Farenheit? ')
solution = (int(temp_F) - 32) * 5/9
print('Temperature in degrees is ', solution)
