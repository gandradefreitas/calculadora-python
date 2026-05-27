"""
Módulo responsável pelo histórico da calculadora.
"""

historico = [] # Guarda o historico de resultado
contador = 0

# Mensagem(print)
def mostrar(resultados):
    """
    Exibe o resultado da operação.
    """
    print(f'\033[1;34mResultado\033[m: {resultados}')

def mostrar_historico():
    """
    Exibe o histórico de operações realizadas.
    """

    ver_historico = input('Deseja ver o seu historico de resultados? [S/N] ').upper()

    if ver_historico == 'S':
        print(f'\033[1;32m{contador}\033[m operações feitas.')
        for conta in historico:
            for valor in conta.values():
                print(f'{valor}', end=' ')
            print()

def registrar_operacao1(num1, operacao, num2, resultado):
    """
    Registra operações realizadas com dois números.

    Args:
        num1 (float): Primeiro número.
        operacao (str): Símbolo da operação.
        num2 (float): Segundo número.
        resultado (float): Resultado da operação.
    """
    global contador

    contas = {
        'num1 escolhido': num1,
        'operação': operacao,
        'num2 escolhido': num2,
        'igual': '=',
        'resultado': resultado
    }

    historico.append(contas)
    mostrar(resultado)
    contador += 1

def registrar_operacao2(nome_operacao, numero, resultado):
    """
    Registra operações realizadas com um número.

    Args:
        nome_operacao (str): Nome da operação.
        numero (float): Número utilizado.
        resultado (float): Resultado da operação.
    """

    global contador

    contas = {
        'operação': nome_operacao,
        'num escolhido': numero,
        'igual': '=',
        'resultado': resultado
    }

    historico.append(contas)
    mostrar(resultado)
    contador += 1
