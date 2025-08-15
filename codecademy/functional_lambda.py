 
square = lambda x: x * x

cube = lambda x: x * x * x

def odd_or_even(n, even_function, odd_function):
  if n % 2 == 0:
    return even_function(n)
  else:
    return odd_function(n)

# test = odd_or_even(5, cube, square)
test = odd_or_even(2, cube, square)
print(test) 