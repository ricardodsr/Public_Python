# Imprime cada fruta da lista
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#Uma string tambem e uma sequencia: imprime cada letra de "banana":
for x in "banana":
    print(x)


# Sai do for quando x e "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Sai do for quando x e "banana", mas desta vez, o break sai antes do print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


# continue salta para a proxima iteracao: imprime apenas os numeros fora de 4..6
# Atencao: usar "and" e nao "&" - o "&" e um operador de bits e e avaliado
# antes das comparacoes, o que muda completamente o resultado.
numeros = [1,2,3,4,5,6,7,8,9]
for x in numeros:
    if x > 3 and x < 7:
        continue
    print(x)



for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")


# Imprime todos os adjectivos para cada fruta:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)




def my_function(fname, lname):
    print(f"{fname} {lname}")


my_function("Cris", "Marcelo")




def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# more arguments and stuff
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")

# returning argumetns


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))
