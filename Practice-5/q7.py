'''Write a Python function called convert_temperature that takes a temperature in Celsius and converts it to Fahrenheit.
 The formula for conversion is: F = (C * 9/5) + 32'''

def fahrenheit():
    celcius=int(input("Enter the temperatue in celcius:"))
    F=((celcius * 9/5) + 32)
    print("Temperature in Fahrehnite is:",F)

fahrenheit()