"""
Módulo responsável pela interface da calculadora.

Contém funções de:
- menu
- leitura de dados
- validação
- controle de continuidade
"""

def continuar():
    """
    Função que pergunta ao usuário se ele quer
    continuar com as operações ou não.

    Returns:
        bool: True para continuar e False para encerrar

    """

    resposta = input('Deseja continuar? (\033[1;34mS\033[m/\033[1;31mN\033[m): ').lower()

    if resposta == 'n':
        print('\033[1;31mFinalizando...\033[m')
        return False
    elif resposta == 's':
        print('\033[1;32mRecomeçando...\033[m')
        return True
    else:
        print('\033[1;31mInválido\033[m!')
        return continuar()

def menu():
    """
    Exibe o menu principal de operações
    da calculadora.
    """

    print('Escolha a operação:\n'
          '[0] \033[1;34mSomar\033[m\n'
          '[1] \033[1;34mMultiplicar\033[m\n'
          '[2] \033[1;34mDividir\033[m\n'
          '[3] \033[1;34mDiminuir\033[m\n'
          '[4] \033[1;34mPotência\033[m\n'
          '[5] \033[1;34mRaiz quadrada\033[m\n'
          '[6] \033[1;34mValor absoluto\033[m\n'
          '[7] \033[1;34mResto da divisão\033[m\n'
          '[8] \033[1;34mDivisão inteira\033[m\n'
          '[9] \033[1;34mLog\033[m\n'
          '[10] \033[1;34mFatorial\033[m\n'
          '[11] \033[1;34mPorcentagem\033[m\n'
          '[12] \033[1;34mSeno\033[m\n'
          '[13] \033[1;34mCosseno\033[m\n'
          '[14] \033[1;34mTangente\033[m\n')

def leiaint(msg):
    """
    Lê e valida um número inteiro digitado pelo usuário.

    Args:
        msg (str): Mensagem exibida na entrada.

    Returns:
        int: Número inteiro informado pelo usuário.
    """
    while True:
        try:
            valor = int(input(msg))
        except ValueError, TypeError:
            print('\033[1;31mERROR: Por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mIntrada de dados interrompida pelo usuário.\033[m ')
            break
        else:
            return valor


def leiafloat(msg):
    """
    Lê e valida um número real digitado pelo usuário.

    Args:
        msg (str): Mensagem exibida na entrada.

    Returns:
        float: Número real informado pelo usuário.
    """

    while True:
        try:
            valor = float(input(msg))
        except ValueError, TypeError:
            print('\033[1;31mERROR: Por favor digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mEntrada de dados interrompida pelo usuário.\033[m ')
            break
        else:
            return valor

