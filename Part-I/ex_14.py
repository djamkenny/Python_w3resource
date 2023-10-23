#Write a Python program to calculate the number of days between two dates.
from datetime import date
firstDate = date(2023,2,23).isoweekday()
secondDate = date(2023,1,22).isoweekday()
days = secondDate - firstDate
print(days)

