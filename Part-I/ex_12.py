#Write a Python program that prints the calendar for a given month and year.
import calendar
yy = int(input('year: '))
mm = int(input('month: '))

print(calendar.month(yy,mm))
