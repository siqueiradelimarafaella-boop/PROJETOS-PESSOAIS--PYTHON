# Enunciado:
# Desenvolva uma calculadora de linha de comando (CLI) em Python.
# O programa deve:

# Exibir um menu de opções com as operações básicas (+, −, ×, ÷).

# Permitir que o usuário digite sua escolha e dois números.

# Realizar a operação correspondente e mostrar o resultado formatado.

# Tratar possíveis erros (como divisão por zero ou entrada inválida).

# Perguntar se o usuário deseja realizar outro cálculo ou sair do programa

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if a == 0 or b == 0:
        return None
    else:    
     return a / b

def main():
    menu = '''
[+] Soma
[-] Subtração
[*] Multiplicação
[/] Divisão
[s] Sair
=> '''

    while True:
        selecao = input(menu)

        if selecao == '+':
            primeiro_numero = float(input('Informe o primeiro valor: '))
            segundo_numero = float(input('Informe o segundo valor: '))
            print(f'A soma é: {soma(primeiro_numero, segundo_numero)}\n')
        elif selecao == '-':
            primeiro_numero = float(input('Informe o primeiro valor: '))
            segundo_numero = float(input('Informe o segundo valor: '))
            print(f'A subtração é: {subtracao(primeiro_numero, segundo_numero)}\n')
        elif selecao == '*':
            primeiro_numero = float(input('Informe o primeiro valor: '))
            segundo_numero = float(input('Informe o segundo valor: '))
            print(f'A multiplicação é: {multiplicacao(primeiro_numero, segundo_numero)}\n')
        elif selecao == '/':
            primeiro_numero = float(input('Informe o primeiro valor: '))
            segundo_numero = float(input('Informe o segundo valor: '))

            resultado = divisao(primeiro_numero, segundo_numero)
            if resultado is not None:
             print(f'A divisão é: {resultado}\n')
            else:
                print ('Operação não pode ser realizada! Divisão por 0')     

        elif selecao == 's':
            print("Encerrando o programa...")
            break
        else: 
            print("\n Operação inválida. Tente novamente.")


main()





