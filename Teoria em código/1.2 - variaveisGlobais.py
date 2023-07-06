
print("Podemos criar variaveis globais para usa-las dentro e fora de funçoes")
print("uso de x , internamente na função\n")
x = "awesome"

def myfunc():
  """
  This function takes no arguments and does not return anything. 
  It prints the string "Python is " concatenated with the value of the variable x.
  """
  print("Python is " + x)

myfunc() 

wait = input("Ler os comentarios no codigo !!! \n Apertar para continuar.\n")

print("Podemos criar variaveis globais para usa-las dentro e fora de funçoes")
print("uso de y , internamente na função, e declaração interna de y\n")

y = "awesome"

def myfunc():
  """
  Prints the string "Python is fantastic" to the console.
  """

  y = "fantastic"
  print("Python is " + y)

myfunc()

print("Python is " + y) 
wait = input("Ler os comentarios no codigo !!! \n Apertar para continuar.\n")


print("Podemos mudar o valor de uma variavel global dentro da função, para isso temos que referir a variavel como global\n")

x = "awesome"

def myfunc():
  """
  Set the global variable `x` to the string "fantastic".
  """
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 
wait = input("Ler os comentarios no codigo !!! \n Apertar para continuar.\n")