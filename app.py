"""
Arquivo principal do servidor Flask.

Responsável por:

- iniciar a aplicação web
- conectar front-end e back-end
- receber requisições do JavaScript
- executar operações matemáticas
- devolver resultados para o navegador
"""

# ===========================================================
#                      IMPORTAÇÕES
# ===========================================================

# Ferramentas principais do Flask
from flask import Flask, render_template, request, jsonify

# Classe principal da calculadora
from classCalculadora import Calculadora

# ============================================================
#                CONFIGURAÇÃO DA APLICAÇÃO
# ============================================================

# Cria a aplicação Flask
app = Flask(__name__)

# Cria o objeto calculadora
calc = Calculadora()

# ============================================================
#                       ROTA PRINCIPAL
# ============================================================

@app.route('/')
def home():
    """
    Renderiza a página principal da calculadora.
    """
    return render_template('index.html')

# ============================================================
#                   OPERAÇÕES INDIVIDUAIS
# ============================================================

@app.route('/somar', methods=['POST'])
def somar():
    """
    Recebe os valores enviados pelo JavaScript,
    executa a soma usando a calculadora
    e devolve o resultado em JSON.
    """

    dados = request.get_json()

    n1 = float(dados['n1'])
    n2 = float(dados['n2'])

    resultado = calc.somar(n1, n2)

    return jsonify({
        'resultado': resultado
    })

@app.route('/multiplicar', methods=['POST'])
def multiplicar():

    dados = request.get_json()

    n1 = float(dados['n1'])
    n2 = float(dados['n2'])

    resultado = calc.multiplicar(n1, n2)
    return jsonify({
        'resultado': resultado
    })

@app.route('/dividir', methods=['POST'])
def dividir():

    dados = request.get_json()

    n1 = float(dados['n1'])
    n2 = float(dados['n2'])

    resultado = calc.dividir(n1, n2)

    return jsonify({
        'resultado': resultado
    })

@app.route('/diminuir', methods=['POST'])
def diminuir():

    dados = request.get_json()

    n1 = float(dados['n1'])
    n2 = float(dados['n2'])

    resultado = calc.diminuir(n1, n2)

    return jsonify({
        'resultado': resultado
    })

# ============================================================
#                 ROTA PRINCIPAL DE CÁLCULO
# ============================================================
@app.route('/calcular', methods=['POST'])
def calcular():
    """
    Recebe os dados enviados pelo JavaScript,
    identifica a operação escolhida e devolve o resultado.
    """

    dados = request.get_json()

    n1 = float(dados['n1'])
    n2 = float(dados['n2'])

    operacao = dados['operacao']

    if operacao == '+':
        resultado = calc.somar(n1, n2)

    elif operacao == '-':
        resultado = calc.diminuir(n1, n2)

    elif operacao == '*':
        resultado = calc.multiplicar(n1, n2)

    elif operacao == '/':
        resultado = calc.dividir(n1, n2)

    return jsonify({
        'resultado': resultado
    })

# ==========================================================
# INICIALIZAÇÃO DO SERVIDOR
# ==========================================================

if __name__ == '__main__':

    # Executa servidor Flask em modo debug
    app.run(debug=True)