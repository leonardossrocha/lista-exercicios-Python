print("==========================================")
# O ':^40' diz ao Python para centralizar o texto em um espaço de 40 caracteres
print(f"|{'SISTEMA DE ONBOARDING ARKETECH':^40}|")
print("==========================================\n")

print("Por favor, preencha seus dados para a geração do crachá:\n")

nome_completo = input("Digite seu nome completo: ")
idade = input("Digite sua idade: ") 
cargo = input("Digite o cargo desejado: ")
email = input("Digite seu e-mail corporativo: ")

print("\n" + "="*42)
print(f"|{'CRACHÁ VIRTUAL':^40}|")
print("="*42)

# Montamos a string de cada linha primeiro
linha1 = f"👤 NOME:  {nome_completo.upper()}"
linha2 = f"🎂 IDADE: {idade} anos"
linha3 = f"💼 CARGO: {cargo.title()}"
linha4 = f"📧 EMAIL: {email.lower()}"

# O ':<38' diz ao Python: "Empurre esse texto para a esquerda e 
# preencha o resto com espaços até dar 38 caracteres".
print(f"| {linha1:<38} |")
print(f"| {linha2:<38} |")
print(f"| {linha3:<38} |")
print(f"| {linha4:<38} |")

print("="*42)
print(f"|{'>> Acesso Liberado. Bem-vindo(a)! <<':^40}|")
print("==========================================")
