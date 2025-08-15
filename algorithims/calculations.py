import math

'''
    write functions that returns a equation total
    *, /, +, -, **, //, %, sqrt, etc;
'''

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Your second number cannot be zero.'
    else:
        result = x / y
        return round(result, 2)

def power(x, y):
    return x ** y

def square_root(x):
    result = math.sqrt(x)
    return round(result, 2)

def remainder(x, y):
    if x <= y:
        return 0
    return x % y

def percentageOf(x: int, percent: int):
    percentage = percent / 100
    return x * percentage

def dicounted_price(price, discount_rate):
    discount = (discount_rate / 100) * price
    total_price = price - discount
    return total_price

def area_of_triangle(base, height):
    return (base * 0.5) * height



# tests
# print('add::: ', add(2, 3))
# print('sub::: ', subtract(2, 3))
# print('mult::: ', multiply(2, 3))
# print('div::: ', divide(2, 3))
# print('pow::: ', power(2, 3))
# print('sqrt::: ', square_root(7))
# print('remainder::: ', remainder(9, 7))
# print('percent::: ', percentageOf(5500, 20))
# print('discounted price::: ', dicounted_price(5500, 20))
# print('area triangle::: ', area_of_triangle(5, 10))
