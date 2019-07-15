'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''

temp_in_f = int(input("Type in a temperature in Fahrenheit "))
temp_in_c = ((temp_in_f - 32) * (5/9))
print("Temp in Centigrade is ", temp_in_c)