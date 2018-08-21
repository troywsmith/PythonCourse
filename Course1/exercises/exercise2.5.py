# Exercise 5: Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the
# converted temperature.

cels = input("What is the temp in Celsius? ")
fahr = int(cels) * (9 / 5) + 32
print("Fahrenheit: ", fahr)