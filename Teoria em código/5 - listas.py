
def listaInicial():
    mylist = ["apple", "banana", "cherry"]
    print(mylist[1])  # acessar elementos da lista
    # indexadores negativos, acessam a lista de forma invertida
    print(mylist[-1])


listaInicial()
wait = input("Apertar para continuar.")


def thislista():
    var = input("digite uma fruta")
    thislist = ["apple", "banana", "cherry", "apple", "cherry"]
    print(thislist)
    print(len(thislist))  # length da lista, ou seja o tamanho da lista
    print(thislist[2:4])  # imprive os elementos da lista 2 a 4
    print(thislist[:4])  # imprime do inicio ate o 4 elemento (nao incluido)
    print(thislist[2:])  # imprime do 2 indexador ate o final da lista

    if var in thislist:  # verificador de elemento na lista
        print("Existe {} na lista".format(var))


thislista()

wait = input("Apertar para continuar.")


def modificandoListas():

    mainlist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    sndlist = ["teste1", "teste2", "teste3"]

    mainlist[1] = "blackcurrant"  # modifica o valor
    print(mainlist)

    mainlist[1:3] = ["blackcurrant", "watermelon"]
    print(mainlist)  # modifica os valores

    mainlist.insert(2, "watermelon")
    print(mainlist)  # insere na segunda posicao

    mainlist.append("orange")
    print(mainlist)  # adiciona no final da lista

    mainlist.extend(sndlist)  # adiciona a snd lista no final da main list
    print(mainlist)


modificandoListas()


wait = input("Apertar para continuar.")


def removendoListas():
    mainlist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    print(mainlist)
    mainlist.remove("banana")
    print(mainlist)
    mainlist.pop(1)
    print(mainlist)


removendoListas()
wait = input("Apertar para continuar.")


def iterandoLista():
    lista = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    for i in range(len(lista)):
        print(lista[i])


iterandoLista()
wait = input("Apertar para continuar.")


def usandoWhile():
    lista = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    i = 0
    while i < len(lista):
        print(lista[i])
        i = i + 1


usandoWhile()
wait = input("Apertar para continuar.")


#Ver com muita calma (isto e mesmo foda)
def compreensao():
    lista = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    [print(x) for x in lista]
compreensao() 
wait = input("Apertar para continuar.")