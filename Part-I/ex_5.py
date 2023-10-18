#Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

#take input form the user
firstname = input('First Name: ')
lastname = input('Last Name: ')
#function that reverse the name 

def reverse(first, last):
    name = first + ' ' + last
    n = ""
    for x in name:
        n = x + n
    return n
newname = reverse(firstname, lastname)
print(newname)

print('if that now tha correct way exactly then:', lastname, firstname)
