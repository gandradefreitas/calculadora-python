"""
Projeto simples de calculadora em Python.

O programa permite realizar operações matemáticas,
registrar histórico e interagir por menu no terminal.

"""

import operacao
import historico
import interface

while True:

    interface.menu()

    op = interface.leiaint('Escolha a operação: ')

    if op == 10:
        n3 = interface.leiaint('Digite o \033[1;34mvalor\033[m: ')
        resultado = operacao.fatorial(n3)
        historico.registrar_operacao2('Fatorial', n3, resultado)
        historico.mostrar_historico()

        if not interface.continuar():
            break

        continue

    if op in [5, 6, 9, 12, 13, 14]:

        n3 = interface.leiafloat('Digite o \033[1;34mvalor\033[m: ')

        if op == 5:
            resultado = operacao.raiz(n3)
            historico.registrar_operacao2('Raiz', n3, resultado)

        elif op == 6:
            resultado = operacao.absoluto(n3)
            historico.registrar_operacao2('Valor Abs', n3, resultado)

        elif op == 9:
            resultado = operacao.log(n3)
            historico.registrar_operacao2('Log', n3, resultado)

        elif op == 12:
            resultado = operacao.seno(n3)
            historico.registrar_operacao2('Seno', n3, resultado)

        elif op == 13:
            resultado = operacao.cosseno(n3)
            historico.registrar_operacao2('Cos', n3, resultado)

        elif op == 14:
            resultado = operacao.tangente(n3)
            historico.registrar_operacao2('Tang', n3, resultado)

        historico.mostrar_historico()

        if not interface.continuar():
            break

        continue

    if op in [0, 1, 2, 3, 4, 7, 8, 11]:


        n1 = interface.leiafloat('Digite o \033[1;34mprimeiro valor\033[m: ')
        n2 = interface.leiafloat('Digite o \33[1;31msegundo valor\033[m: ')

        if op == 0:
            resultado = operacao.somar(n1, n2)
            historico.registrar_operacao1(n1, '+', n2, resultado)

        elif op == 1:
            resultado = operacao.multiplicar(n1, n2)
            historico.registrar_operacao1(n1, '*', n2, resultado)

        elif op == 2:
            if n2 != 0:
                resultado = operacao.dividir(n1, n2)
                historico.registrar_operacao1(n1, '/', n2, resultado)
            else:
                print('\033[1;31mErro\033[m: divisão por 0!')

        elif op == 3:
            resultado = operacao.diminuir(n1, n2)
            historico.registrar_operacao1(n1, '-', n2, resultado)

        elif op == 4:
            resultado = operacao.potencia(n1, n2)
            historico.registrar_operacao1(n1, '^', n2, resultado)

        elif op == 7:
            resultado = operacao.resto(n1, n2)
            historico.registrar_operacao1(n1, '%', n2, resultado)

        elif op == 8:
            resultado = operacao.div_inteira(n1, n2)
            historico.registrar_operacao1(n1, '//', n2, resultado)

        elif op == 11:
            resultado = operacao.porcentagem(n1, n2)
            historico.registrar_operacao1(n1, '%', n2, resultado)

    else:
        print('\033[1;31mOperação invalida\033[m!')

    historico.mostrar_historico()

    if not interface.continuar():
        break


