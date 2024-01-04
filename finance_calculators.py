"""
import math function

print a statement to describe the options - 'investment' and 'bond'
request the user input and store in a variable, allowing for both upper/lower case entries

if the user enters 'investment', store inputs as corresponding variables for the equations 
store the provided equations as variables named 'simple_interest' and 'compound_interest'
request user to input the interest option and store as a variable named 'interest'
create if statement to print the relevant results rounded to two decimal places

if the user enters 'bond' - store inputs as the corresponding variables for the equation   
store the 'bond' equation as the variable 'repayment'
print the result rounded to two decimal places

print error message if user input is not 'investment' or 'bond'
"""

# imported the math function
import math

# printed a statement to describe the interest options
print ("Investment - to calculate the amount of interest you'll earn on your investment")
print ("Bond - to calculate the amount you'll have to pay on a home loan")

# stored the requested user input in a variable, allowing for upper/lower case
user_selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").upper().lower()

# if 'investment' - stored inputs as the corresponding variables for the equations
if user_selection == ("investment"):
    P = float(input("Please enter the deposit amount in digits: "))
    r = float(input("Please enter the interest rate in digits: ")) / 100 #divided 'r' by 100
    t = float(input("Please enter the yearly duration of the investment in digits: "))

# stored the 'investment' equations as variables
    simple_interest = A = P *(1 + r*t)
    compound_interest = A = P * math.pow((1+r), t)

# requested user to input interest option and stored as a variable named 'interest'
    interest = input("Please enter the interest option. Type 'simple' or 'compound': ").upper().lower()

# created if statement to print the relevant results rounded to two decimal places
    if interest == "simple":
        print (f"You will earn £{round(simple_interest, 2)}")
    elif interest == "compound":
        print (f"You will earn £{round(compound_interest, 2)}")

# if 'bond' - stored inputs as the corresponding variables for the equations
elif user_selection == ("bond").upper().lower():
    P = float(input("Please enter the current valuation of the property: "))
    i = float(input("Please enter the interest rate in digits: ")) / 100 / 12 #divided by 100 then by 12
    n = float(input("Please enter the duration of repayment in months: "))

# stored the 'bond' equation as the variable 'repayment'
    repayment = (i * P)/(1 - (1 + i)**(-n))

# printed the result rounded to two decimal places
    print(f"You will have to pay £{round(repayment, 2)} per month.")

# printed error message if user input is not 'investment' or 'bond'
else:
    print("Error - input not recognised!")
