/* ==================================================
            CALCULADORA WEB - JAVASCRIPT
   ==================================================

   Responsável por:

   - controlar o visor da calculadora
   - adicionar números
   - adicionar operadores
   - enviar cálculos para o Flask
   - receber resultados do back-end
   - atualizar o visor
*/

// ==================================================
//             FUNÇÕES DO VISOR
// ==================================================

/* Adiciona números ao visor. */
function adicionarNumero(numero) {

    let visor = document.getElementById('visor')

    visor.value += numero
}

/* Adiciona operadores matemáticos ao visor. */
function adicionarOperador(operador) {

    let visor = document.getElementById('visor')

    visor.value += operador
}

// ==================================================
//           FUNÇÃO PRINCIPAL DE CÁLCULO
// ==================================================

/*
Captura a expressão digitada,
identifica a operação, envia os dados para o Flask
e mostra o resultado no visor.
*/
async function calcular() {

    // Captura visor
    let visor = document.getElementById('visor')

    // Captura expressão completa
    let expressao = visor.value

    // Variável da operação
    let operador

    // Identifica operador utilizado
    if (expressao.includes('+')) {
        operador = '+'
    }

    else if (expressao.includes('-')) {
        operador = '-'
    }

    else if (expressao.includes('*')) {
        operador = '*'
    }

    else if (expressao.includes('/')) {
        operador = '/'
    }

    // Divide a expressão
    let partes = expressao.split(operador)

    // Primeiro número
    let n1 = partes[0]

    // Segundo número
    let n2 = partes[1]

    // Envia dados para o Flask
    let resposta = await fetch('/calcular', {

        method: 'POST',

        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify({

            n1: n1,
            n2: n2,
            operacao: operador
        })
    })

    // Recebe resposta do Flask
    let dados = await resposta.json()

    // Mostra resultado no visor
    visor.value = dados.resultado
}