print("="*42)
print(f"|{'SISTEMA DE OMBOARDING':^40}|")
# o '^40' diz ao Python para centralizar
#o texto em um espaço de 40 caracteres
print("="*42)

print("Por favor, preencha seus dados para a \ngeração do crachá:\n")
nome = input("Digite seu nome: ")
idade= input("Informe sua idade: ")
cargo= input("Digite seu cargo: ")
email= input("Digite seu e-mail: ")

print("="*42)
print(f"|{'CRACHÁ VIRTUAL':^40}|")
print("="*42)

# Montando string com dados informados pelo usuario
linha1 = f" NOME:  {nome}"
linha2 = f" IDADE: {idade} anos"
linha3 = f" CARGO: {cargo}"
linha4 = f" EMAIL: {email}"
# O :<38 diz ao python para empurrar o texto para a esquerda
# e preencher de espaços até dar 38 caracteres
print(f"| {linha1:<38} |")
print(f"| {linha2:<38} |")
print(f"| {linha3:<38} |")
print(f"| {linha4:<38} |")

print("="*42)
print(f"|{'>> Acesso Liberado. Bem-vindo(a)! <<':^40}|")
print("="*42)
