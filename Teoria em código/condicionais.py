"""
    Equals: a == b
    Not Equals: a != b
    Less than: a < b
    Less than or equal to: a <= b
    Greater than: a > b
    Greater than or equal to: a >= b
"""
a = 33
b = 200
if b > a:
  print("b is greater than a")

wait = input("Apertar para continuar.")

def minhaprimeirafuncao():
    x = 10
    if x >= 18:
        print ("maior de idade")
    if x > 18 and x == 32 :
        print ("idade perfeita")
    elif x < 18:
        print("menor idade")
minhaprimeirafuncao()

wait = input("Apertar para continuar.")


def parOuImpar():
    y = 10
    if y % 2 == 0:
        print ("par")
    else:
        print ("impar")
parOuImpar()

wait = input("Apertar para continuar.")

def maior():
    lista = [5,2,3]
    a,b,c = lista
    if a > b and a > c :
        print (a)
    elif b > a and b > c :
        print (b)
    else:
        print (c)
maior()
wait = input("Apertar para continuar.")

def maiorPro():
    lista = [1,2,3,4,5,6,7,8,9]
    for x in lista:
        print(x)
maiorPro()
wait = input("Apertar para continuar.")