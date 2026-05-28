"""
Módulo principal da calculadora.

Este arquivo contém a classe Calculadora,
responsável por:

- Executar o fluxo principal do programa
- Realizar operações matemáticas
- Registrar operações no histórico
- Exibir resultados
- Controlar a interação principal da calculadora

A classe também organiza operações de:
- Um número
- Dois números
- Histórico de operações
- Tratamento de erros
"""

import math
import interface

class Calculadora:
    """
    Classe responsável pelo funcionamento
    completo da calculadora.

    Armazena:
    - histórico de operações
    - contador de operações

    Também executa:
    - operações matemáticas
    - exibição de resultados
    - controle do menu principal
    """

    def __init__(self):
        self.historico = []
        self.contador = 0


    def executar_operacao(self):

        operacoes_um_valor = self.operacoes1()
        operacoes_dois_valores = self.operacoes2()

        while True:

            interface.menu()

            op = interface.leiaint('Escolha a operação: ')

            # Operações com um valor.
            if op in operacoes_um_valor:

                nome, funcao = operacoes_um_valor[op]

                if op == 10:
                    n3 = interface.leiaint('Digite o \033[1;34mvalor\033[m: ')
                else:
                    n3 = interface.leiafloat('Digite o \033[1;34mvalor\033[m: ')

                try:
                    resultado = funcao(n3)
                except (ValueError, TypeError):
                    print('\033[1;31mERRO: Digite um valor válido\033[m')
                else:
                    self.registrar_operacao2(nome, n3, resultado)
                    self.mostrar_historico()

            # Operações com dois valores.
            elif op in operacoes_dois_valores:

                nome, funcao = operacoes_dois_valores[op]

                n1 = interface.leiafloat('Digite o \033[1;34mprimeiro valor\033[m: ')
                n2 = interface.leiafloat('Digite o \033[1;31msegundo valor\033[m: ')

                try:
                    resultado = funcao(n1, n2)
                except ZeroDivisionError:
                    print('\033[1;31mERRO: Divisão por zero\033[m')
                else:
                    self.registrar_operacao1(n1, nome, n2, resultado)
                    self.mostrar_historico()

            else:
                print('\033[1;31mOperação inválida\033[m!')

            if not interface.continuar():
                break



    # Mensagem(print)

    def mostrar(self, resultados):
        """
        Exibe o resultado da operação.
        """
        print(f'\033[1;34mResultado\033[m: {resultados}')


    def mostrar_historico(self):
        """
        Exibe o histórico de operações realizadas.
        """

        ver_historico = input('Deseja ver o seu historico de resultados? [S/N] ').upper()

        if ver_historico == 'S':
            print(f'\033[1;32m{self.contador}\033[m operações feitas.')
            for conta in self.historico:
                for valor in conta.values():
                    print(f'{valor}', end=' ')
                print()

    def registrar_operacao1(self, num1, operacao, num2, resultado):
        """
        Registra operações realizadas com dois números.

        Args:
            num1 (float): Primeiro número.
            operacao (str): Símbolo da operação.
            num2 (float): Segundo número.
            resultado (float): Resultado da operação.
        """

        contas = {
            'num1 escolhido': num1,
            'operação': operacao,
            'num2 escolhido': num2,
            'igual': '=',
            'resultado': resultado
        }

        self.historico.append(contas)
        self.mostrar(resultado)
        self.contador += 1

    def registrar_operacao2(self, nome_operacao, numero, resultado):
        """
        Registra operações realizadas com um número.

        Args:
            nome_operacao (str): Nome da operação.
            numero (float): Número utilizado.
            resultado (float): Resultado da operação.
        """

        contas = {
            'operação': nome_operacao,
            'num escolhido': numero,
            'igual': '=',
            'resultado': resultado
        }

        self.historico.append(contas)
        self.mostrar(resultado)
        self.contador += 1

    # Operações matemáticas

    # Primeira parte: cálculos com dois números

    def somar(self, a, b):
        """Retorna a soma entre dois números."""
        return a + b


    def multiplicar(self, a, b):
        """Retorna a multiplicação entre dois números."""
        return a * b


    def dividir(self, a, b):
        """Retorna a divisão entre dois números."""
        return a / b


    def diminuir(self, a, b):
        """Retorna a subtração entre dois números."""
        return a - b


    def potencia(self, a, b):
        """Retorna a potência entre dois números."""
        return math.pow(a, b)


    def resto(self, a, b):
        """Retorna o resto da divisão."""
        return a % b


    def div_inteira(self, a, b):
        """Retorna a divisão inteira."""
        return a // b


    def porcentagem(self, a, b):
        """Calcula a porcentagem de um valor."""
        return (a * b) / 100

    def operacoes2(self):
        """
        Retorna um dicionário com operações
        matemáticas que utilizam dois números.
        """
        return {
            0: ('+', self.somar),
            1: ('*', self.multiplicar),
            2: ('/', self.dividir),
            3: ('-', self.diminuir),
            4: ('^', self.potencia),
            7: ('%', self.resto),
            8: ('//', self.div_inteira),
            11: ('%', self.porcentagem),
        }

    # Segunda parte: cálculos com um número

    def raiz(self, a):
        """Retorna a raiz quadrada do número."""
        return math.sqrt(a)


    def absoluto(self, a):
        """Retorna o valor absoluto."""
        return math.fabs(a)


    def log(self, a):
        """Retorna o logaritmo natural."""
        return math.log(a)


    def fatorial(self, a):
        """
        Retorna o fatorial de um número inteiro.
        """
        return math.factorial(a)


    def seno(self, a):
        """Retorna o seno do ângulo em graus."""
        return math.sin(math.radians(a))


    def cosseno(self, a):
        """Retorna o cosseno do ângulo em graus."""
        return math.cos(math.radians(a))


    def tangente(self, a):
        """Retorna a tangente do ângulo em graus."""
        return math.tan(math.radians(a))

    def operacoes1(self):
        """
        Retorna um dicionário com operações
        matemáticas que utilizam apenas um número.
        """

        return {
            5: ('Raiz', self.raiz),
            6: ('Valor Abs', self.absoluto),
            9: ('Log', self.log),
            10: ('Fatorial', self.fatorial),
            12: ('Seno', self.seno),
            13: ('Cos', self.cosseno),
            14: ('Tang', self.tangente)
        }