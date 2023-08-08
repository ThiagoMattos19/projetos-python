import random

chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()-=" #Caracteres que vão ser gerados na senha

print("=============BEM VINDO AO GERADOR DE SENHAS=============")

numero = input("Digite o numero de senhas que você vai querer:") #Quantidades de senhas que vão ser geradas
numero = int(numero)

tamanho = input("Digite o tamanho da senha: ") #tamanho das senhas que vão ser geradas
tamanho = int(tamanho)

print('\nAqui está a sua senha: ')

for snh in range(numero): #Estrutura de repetição que vai gerar a quantidade de senhas
    senha = ''

    for c in range(tamanho): #estrutura de repetição que ira definir o tamanho da senha
        senha += random.choice(chars) #comando que irá aleatorizar as senhas gerada
    print('========================================================')
    print(senha)
    print("========================================================")

