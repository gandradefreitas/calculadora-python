"""
Arquivo principal da aplicação.

Responsável por iniciar a calculadora
e executar o programa.
"""

from classCalculadora import Calculadora

def main():

    calc = Calculadora()
    calc.executar_operacao()

if __name__ == '__main__':
    main()