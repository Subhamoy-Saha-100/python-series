# Write a python program to display a user entered name followed by Good Afternoon using
# input() function.
from datetime import date, datetime

# name = input("Enter your name :- ")
# greeting = "Good Afternoon, "
# # print(greeting + name)

# Date = date.today()

# letter = f'''
# Dear {name},
# You are selected!
# {Date}
# '''

# print(letter)

# Write a program to detect double space in a string.

str = "Hey      friend"
hasDoubleSpace = str.find("  ")

# if hasDoubleSpace+1:
#     print("have")
# else:
#     print("Don't have")

str = str.replace("  ", " ")
print(str)
