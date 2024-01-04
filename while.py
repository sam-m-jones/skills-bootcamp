"""
request user to input any positive integer
create list to store input
store input in the list

create while loop

repeat request for user input and store in the list
if input is -1, remove -1 from the list and print a command to stop

calculate and print the average of the list
"""

# requested user to input any integer
number = int(input("Enter any positive integer: "))

# created list to store input
numbers_list = []
numbers_list.append(number)

while number > 0:
    numbers = int(input("Enter another positive integer: "))
    numbers_list.append(numbers)

# if input is -1
    if numbers == -1:
        print ("Please wait...")

        x = -1
        numbers_list.remove(x)
       # calculated the average of the list
        average = sum(numbers_list) / len(numbers_list)

       # printed a statement to display the average
        print(f"Your average is: {average}")

        break
