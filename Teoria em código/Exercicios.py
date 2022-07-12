# Crie um script Python que leia o nome de uma pessoa e mostre uma 
#mensagem de boas-vindas de acordo com o valor digitado

entrada = input("Digite seu nome: \n")
print("Olá, {}! Vamos começar os exercicios!".format(entrada))
wait = input("Digitar ENTER para continuar.")


# Crie um script Python que leia o dia, o mês e o ano de nascimento de 
#uma pessoa e mostre uma mensagem com a data formatada

ano = int(input("Ano de nascimento: \n"))
mes = int(input("Mês de nascimento: \n"))
dia = int(input("Dia de nascimento: \n"))

print("A pessoa nasceu em: {}/{}/{}".format(dia, mes, ano))
print("A pessoa nasceu no dia {} do mês {} do ano de {}.".format(dia, mes, ano))
print("Esta pessoa tem: {}".format(2021-ano))
wait = input("Digitar ENTER para continuar.")

# Crie um script Python que leia dois números e tente mostrar a soma entre eles

num1 = int(input("Primeiro número: \n"))
num2 = int(input("Segundo número: \n"))
print("A soma é:", num1 + num2)
print("A soma é: %d" % (num1 + num2))
print("A soma é: {}".format(num1 + num2))

# Os três formatos de print aceitam operações entre variáveis
wait = input("Digitar ENTER para continuar.")


# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

entrada = input("Digite algo: \n")
print("Tipo primitivo: {}.".format(type(entrada)))

print("É numérico? {}".format(entrada.isnumeric()))
print("É alfanumérico? {}.".format(entrada.isalpha()))
print("É um decimal? {}.".format(entrada.isdecimal()))
print("Está em caixa baixa? {}.".format(entrada.islower()))
print("É apenas espaço em branco? {}.".format(entrada.isspace()))
print("Está em caixa alta? {}.".format(entrada.isupper()))
wait = input("Digitar ENTER para continuar.")