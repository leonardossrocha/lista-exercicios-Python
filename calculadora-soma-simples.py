"""
PROJETO: Calculadora de Soma Simples
VERSÃO: 1.2.0
DESCRIÇÃO: Este script solicita dois números ao usuário, realiza a 
           operação aritmética de adição e exibe o resultado final.
AUTOR: Leonardo Rocha
"""

def executar_soma():
    print("--- Iniciando Somador Python v1.2.0 ---")
    
    try:
        # Solicita os dados e converte para ponto flutuante
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Realiza o cálculo
        soma = num1 + num2

        # Exibe o resultado com formatação limpa
        print(f"\n> Sucesso! A soma de {num1} + {num2} é: {soma}")
        
    except ValueError:
        # Tratamento de erro caso o usuário digite letras
        print("Erro: Por favor, insira apenas números válidos.")

if __name__ == "__main__":
    executar_soma()
