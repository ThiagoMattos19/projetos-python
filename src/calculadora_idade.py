import datetime



def cor():
    return {'limpa':'\033[m',
             'azul':'\033[34m',
             'amarelo':'\033[33m',
             'pretoebranco':'\033[7;30m'
             }


while True:
    limpar = '\033[m'
    ano_nascimento = int(input("Digite o ano do seu nascimento"))
    ano_atual = int(input("Digite o ano atual"))


    idade_aproximada = ano_atual - ano_nascimento


    print(f' Sua idade é {idade_aproximada}{limpar}', cor()['amarelo'])
