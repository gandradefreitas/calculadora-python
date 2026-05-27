"""
Módulo responsável pelas operações matemáticas
da calculadora.
"""

import math


# Primeira parte: cálculos com dois números

def somar(a, b):
    """Retorna a soma entre dois números."""
    return a + b


def multiplicar(a, b):
    """Retorna a multiplicação entre dois números."""
    return a * b


def dividir(a, b):
    """Retorna a divisão entre dois números."""
    return a / b


def diminuir(a, b):
    """Retorna a subtração entre dois números."""
    return a - b


def potencia(a, b):
    """Retorna a potência entre dois números."""
    return math.pow(a, b)


def resto(a, b):
    """Retorna o resto da divisão."""
    return a % b


def div_inteira(a, b):
    """Retorna a divisão inteira."""
    return a // b


def porcentagem(a, b):
    """Calcula a porcentagem de um valor."""
    return (a * b) / 100

def operacoes2():
    """
    Retorna um dicionário com operações
    matemáticas que utilizam dois números.
    """
    return {
        0: ('+', somar),
        1: ('*', multiplicar),
        2: ('/', dividir),
        3: ('-', diminuir),
        4: ('^', potencia),
        7: ('%', resto),
        8: ('//', div_inteira),
        11: ('%', porcentagem),
    }

# Segunda parte: cálculos com um número

def raiz(a):
    """Retorna a raiz quadrada do número."""
    return math.sqrt(a)


def absoluto(a):
    """Retorna o valor absoluto."""
    return math.fabs(a)


def log(a):
    """Retorna o logaritmo natural."""
    return math.log(a)


def fatorial(a):
    """
    Retorna o fatorial de um número inteiro.
    """
    return math.factorial(a)


def seno(a):
    """Retorna o seno do ângulo em graus."""
    return math.sin(math.radians(a))


def cosseno(a):
    """Retorna o cosseno do ângulo em graus."""
    return math.cos(math.radians(a))


def tangente(a):
    """Retorna a tangente do ângulo em graus."""
    return math.tan(math.radians(a))

def operacoes1():
    """
    Retorna um dicionário com operações
    matemáticas que utilizam apenas um número.
    """

    return {
        5: ('Raiz', raiz),
        6: ('Valor Abs', absoluto),
        9: ('Log', log),
        10: ('Fatorial', fatorial),
        12: ('Seno', seno),
        13: ('Cos', cosseno),
        14: ('Tang', tangente)
    }