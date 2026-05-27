"""
Arquivo principal da calculadora.

Responsável pelo fluxo principal do programa,
interação com o usuário e integração entre
os módulos de operações, histórico e interface.
"""

import operacao
from Projeto_Calculadora_V2 import historico, interface


def main():

    operacoes_um_valor = operacao.operacoes1()
    operacoes_dois_valores = operacao.operacoes2()

    while True:

        interface.menu()

        op = interface.leiaint('Escolha a operação: ')

        #Operações com um valor.
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
                historico.registrar_operacao2(nome, n3, resultado)
                historico.mostrar_historico()

        #Operações com dois valores.
        elif op in operacoes_dois_valores:

            nome, funcao = operacoes_dois_valores[op]

            n1 = interface.leiafloat('Digite o \033[1;34mprimeiro valor\033[m: ')
            n2 = interface.leiafloat('Digite o \033[1;31msegundo valor\033[m: ')

            try:
                resultado = funcao(n1, n2)
            except ZeroDivisionError:
                print('\033[1;31mERRO: Divisão por zero\033[m')
            else:
                historico.registrar_operacao1(n1, nome, n2, resultado)

                historico.mostrar_historico()

        else:
            print('\033[1;31mOperação inválida\033[m!')

        if not interface.continuar():
            break
if __name__ == '__main__':
    main()