'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
#Tested 10-08-2019

carry_on = "c"
while carry_on == "c":
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        print(f"Answer is {num1/num2}")
    except ValueError:
        print("Please type a float for both values: ")
    except ZeroDivisionError:
        print("Please type a non zero denominator")
    finally:
        carry_on = input("Press q to quit or c to carry on: ")

