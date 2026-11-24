print("="*42)
print(f"|{'SISTEMA DE INVESTIMENTOS':^40}|")
# o '^40' diz ao Python para centralizar
#o texto em um espaço de 40 caracteres
print("="*42)

print("Por favor, preencha seus dados para a \ngeração do crachá:\n")
nome = input("Digite seu nome: ")
dt_nasc= input("Informe sua data de nascimento: ")
salario= input("Digite seu salário: ")

print("="*42)
print(f"|{'CÁLCULO DE INVESTIMENTOS':^40}|")
print("="*42)

# Calculo de investimentos
"""
linha1 = f" NOME:  {nome}"
linha2 = f" IDADE: {idade} anos"
linha3 = f" CARGO: {cargo}"
linha4 = f" EMAIL: {email}"
"""
valor = (float(salario) * 0.2)
print(f"Olá, {nome}")
print(f"Nascido em {dt_nasc}: ")
print(f"Você deve investir 20% de sua renda, que\nrepresenta o valor de: {valor:.2f} reais")

print("="*42)
print(f"|{'>> Faça bons investimentos! <<':^40}|")
print("="*42)
