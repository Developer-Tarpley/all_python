import math

# string data type

# literal assignment
first = "Corey"
last = "Tarpley"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("Spinach")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was checking in.

                      All good?

'''
print(multiline)

# escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace('good', 'ok'))
print(multiline)

print(len(multiline))
multiline += "                           "
multiline = "                                      " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print(" ")
# build a menu
title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".") + "$1".rjust(4))
print("muffin".ljust(16, ".") + "$2".rjust(4))
print("cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")
# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some methods return boolean data
print(first.startswith("C"))
print(first.endswith("Z"))

# boolean data tyoe
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# numeric data types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float tyoes
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex types
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in function for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1)) # round up decimal place


print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa)) # rounded up
print(math.floor(gpa)) # rounded down

# casting a  string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
#zip_value = int("New York")