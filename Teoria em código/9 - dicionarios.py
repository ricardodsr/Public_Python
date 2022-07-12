def primeiroDicionario():
    thisdict =	{
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(thisdict)

    print(thisdict["brand"])#imprime brand
    print(thisdict["model"])#imprime model
    print(thisdict["year"])#imprime year
    print(len(thisdict))#tamanho do conteudo do dicionario
primeiroDicionario()


def segundoDict():
    thisdict2 =	{
        "brand": "Ford",
        "electric": False,
        "year": 1964,
        "colors": ["red", "white", "blue"]
    }   
    print(thisdict2) #imprime dicionario

    x = thisdict2["colors"] #x fica com o valor das cores
    print(x)

    y = thisdict2.get("brand") #x fica com o valor do brand
    print(y)

    z = thisdict2.values() # z fica com todos os valores do dicionario completo
    print(z)

    var =  thisdict2.items() # var fica com tuplos de valores tipo - valor
    print(var)
    
segundoDict()

def conteudo():
    dictCont = {
        "nome": "Ricardo",
        "bi"  : 123456789,
        "data nascimento":1981,
        "especialidade": "programador",
        "linguagens": ["Haskell", "C", "Prolog", "Python", "Java"]
    }
    print(dictCont)

    k = dictCont.get("linguagens")
    print(k)

    l = dictCont.items()
    print(l)
conteudo()