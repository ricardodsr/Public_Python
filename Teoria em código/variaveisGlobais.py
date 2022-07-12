
print("Podemos criar variaveis globais para usa-las dentro e fora de funçoes")
print("uso de x , internamente na função\n")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() 

wait = input("Ler os comentarios no codigo !!! \n Apertar para continuar.\n")

print("Podemos criar variaveis globais para usa-las dentro e fora de funçoes")
print("uso de y , internamente na função, e declaração interna de y\n")

y = "awesome"

def myfunc():
  y = "fantastic"
  print("Python is " + y)

myfunc()

print("Python is " + y) 
wait = input("Ler os comentarios no codigo !!! \n Apertar para continuar.\n")


print("Podemos mudar o valor de uma variavel global dentro da função, para isso temos que referir a variavel como global\n")

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 
wait = input("Ler os comentarios no codigo !!! \n Apertar para continuar.\n")