def isLeapYear(year):
  if(year % 4 == 0 and year % 100 !=0) or yea % 400 == 0:
    return True
    return False

year = int(input("Enter a year:"))
if isLeapYear:
  print(year," is a leap year.")
else:
  print(year," is not a leap year.")