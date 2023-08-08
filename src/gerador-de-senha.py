import random

print("Bem vindo ao gerador de senha")

chars = 'abcdefghjiklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*()_+'

numero = input('quantas senhas você vai querer: ')
numero = int(numero)

tamanho = input("Digite o tamanho da senha: ")
tamanho = int(tamanho)

print('\nAqui está sua senha: ')

for snh in range(numero):
    senha = ''
    for c in range(tamanho):
        senha += random.choice(chars)
    print(senha)
