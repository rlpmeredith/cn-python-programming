'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

inv_amount = int(input("Enter investment amount in whole $$$$ "))
int_rate = int(input("Enter interest rate in whole % "))
years = int(input("Enter whole number of years "))
future_value = inv_amount * ((1 + int_rate/100) ** years)
print("The future value is ", future_value)

