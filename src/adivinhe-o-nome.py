import random

print('Bem vindo ao adivinhador de palavras')

nome = input("Digite o seu nome: ")
print(f'Boa sorte {nome}:')

palavras = ['mousepad', 'fone', 'monitor', 'teclado','mouse']

palavra = random.choice(palavras)

print("Adivinhe a palavra".lower())

tentativas = ''

turnos = 12


while turnos > 0:

    falhou = 0

    for p in palavra:
     if p in tentativas:
        print(p)
     else:
        print("_")
        falhou += 1
    
    if falhou == 0:
        print("você venceu!")
        print(f"a palavra era {palavra}")
        break
    
    adivinhe = input("Adivinhe um periférico:")
    tentativas += adivinhe

    if adivinhe not in palavras:
        turnos -=1
        print('errou')
        print(f'você ainda tem {turnos} turnos')

        if turnos == 0:
            print('você perdeu')
    
