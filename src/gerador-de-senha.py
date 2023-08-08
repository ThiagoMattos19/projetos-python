import random

chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()-="

print("=============BEM VINDO AO GERADOR DE SENHAS=============")

numero = input("Digite o numero de senhas que você vai querer:")
numero = int(numero)

tamanho = input("Digite o tamanho da senha: ")
tamanho = int(tamanho)

print('\nAqui está a sua senha: ')

for snh in range(numero):
    senha = ''
    for c in range(tamanho):
        senha += random.choice(chars)
    print('========================================================')
    print(senha)
    print("========================================================")

