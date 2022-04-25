# find out whether a year is leap year or not
year = input("Enter the year :")
result = float(year) % 4
if result != int():
    print(year + " " + ': not a leap year')
else:
    print(year + " " + ": a leap year")
