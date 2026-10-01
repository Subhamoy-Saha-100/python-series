# print(name[-5], name[-4], name[-3], name[-2], name[-1])
# print(name[0:3])

word = "amazing"

word[1:6:2] # mzn
word[-7:-1] # amazin
word[:-7] # amazing
word[0:] # amazing


str = "harry"
# print(str.endswith("rry")) # true
count = str.count("r") 
# count = 2

capitalized = str.capitalize()
# print(capitalized) # output: Harry....... capitalize() = capitalizes the first character.


# find() returns the index of first occurance
index = str.find("rr")
# print(index) Output: 2

replaced = str.replace("r", "l")

# print(replaced) Output: hally

