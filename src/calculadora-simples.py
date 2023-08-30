import textwrap


def menu():
    menu = """Selecione uma opção
    [1] Adição
    [2] subtração
    [3] multiplicação
    [4] divisão
    [5] potenciação
    [6] Sair
    Comando => """

    return input(textwrap.dedent(menu))


def adicao():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print("soma = ", x + y)


def subtracao():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print("subtração = ", x - y)


def multiplicacao():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print("multiplicação = ", x * y)


def divisao():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print("divisão = ", x / y)


def potenciacao():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    print("potencia = ", x ** y)


def main():

    while True:
        opcao = menu().lower()

        if opcao == '1':
            adicao()

        elif opcao == '2':
            subtracao()

        elif opcao == '3':
            multiplicacao()

        elif opcao == '4':
            divisao()

        elif opcao == '5':
            potenciacao()

        elif opcao == '6':
            break

        else:
            print("Digite uma opção válida")


main()
