# python program to check if year is a leap_year or not
year = 2000

# To get year (interger input) from the user
# year =int(input("Enter a year:")
	
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap_year 
if(year%400 ==0) and (year%100 ==0):
    print("{0} is a leap_year".format (year))

# not divided by 100 means not a century year
# year divided by 4 is a leap_year 
elif(year%4 ==0) and (year%100 == 0):
    print("{0} is a leap_year".format (year))
 
 # if not divided by both 400 (century year and 4 (not century)) 
 # year is not leap_year 
 
else:
     print("{0} is not a leap_year".format (year))
