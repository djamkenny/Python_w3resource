#Write a Python program that accepts a filename from the user and prints the extension of the file.

filename = input('filename: ')
name, extension = filename.split('.')
print(extension)
