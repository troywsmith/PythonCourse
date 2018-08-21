# Exercise 3: Write a program to prompt the user for hours and rate per
# hour to compute gross pay.

hrs = input("Enter Hours:")
rate = input("Enter the rate: ")
pay = int(hrs) * float(rate)
print("Pay:", pay)