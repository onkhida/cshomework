# Create a text file with several lines of text in a text editor (for example NotePad).
# Write a program to read this text file and output the contents.
with open('data.txt') as f:
    print(f.read())