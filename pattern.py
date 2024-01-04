"""
define "*" in a variable named 'stars'
create loop for 'i' in the range of 0-9
if 'i' is 4 or less - print stars + "*"
elif 'i' is more than 4 - store '9-i' in a variable named 'index' and print stars with index
"""

# defined "*" in a variable named 'stars'.
stars = "*"

# created loop for 'i' in the range of 0-9.
for i in range(0 , 9):
    if i <= 4:
        print(stars)
        stars = stars +"*"

# elif 'i' is more than 4.
    elif i >= 4:
        index = 9-i
        print(stars[0:index])
