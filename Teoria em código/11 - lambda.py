#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6)) 

#Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 


#Examples::
def myfunc(n):
  """
  A function that takes an integer `n` as a parameter and returns a lambda function that multiplies the input `a` by `n`.

  Parameters:
    - n (int): The integer value to be multiplied by `a`.

  Returns:
    - lambda function: A lambda function that takes an input `a` and returns the product of `a` and `n`.
  """
  return lambda a : a * n

mydoubler = myfunc(2) 

print(mydoubler(11))


#Examples:::
def myfunc1(n):
  """
  A function that takes an integer `n` as a parameter and returns a lambda function that multiplies its argument `a` by `n`.
  """
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
