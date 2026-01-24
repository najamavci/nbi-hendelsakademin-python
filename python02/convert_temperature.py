'''
Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.
Version 1, exempel på output:

Skriv in en temperatur i grader Celsius: 22
Det blir 71.6 grader Fahrenheit.

'''
temperature_unit = str(input("Do you want to give the input in Celsius or in Fahrenheit? Write C, for Celsius, or F, for Fahrenheit. "))

if temperature_unit == "c":
    temperature = float(input("Write temperature in Celsius "))
    converted_temperature = (temperature * 9 / 5) + 32
    if converted_temperature < 50:
        print("The temperature is " + str(converted_temperature) + " degrees outside. Wear some warm clothes!")
    elif converted_temperature > 68:
        print("The temperature is " + str(converted_temperature) + " degrees outside. A day for a swimsuit!")
elif temperature_unit == "f":
    temperature = float(input("Write temperature in Fahrenheit. "))
    converted_temperature = (temperature - 32) * 5 / 9
    if converted_temperature < 10:
        print("The temperature is " + str(converted_temperature) + " degrees outside. Wear some warm clothes!")
    elif converted_temperature > 20:
        print("The temperature is " + str(converted_temperature) + " degrees outside. A day for a swimsuit!")
else: print("OOPS,Wrong input. Please, try again!")