#--------------------GLOBAL--------------------#
lista = []  # define uma variável para a lista

# Lê os dados do arquivo e carrega na lista (com seek(0) para ler do início)
with open("agenda.csv", "a+", encoding="utf-8") as arq2:
    arq2.seek(0)
    lista = arq2.readlines()
#-----------------------------------------------#


def menu():
    print("\n" + "=" * 50)
    print("""\nAGENDA ELETRÔNICA\n
             Escolha a opção:
             (1) Inserir contato
             (2) Deletar
             (3) Mostrar agenda
             (4) Finalizar programa\n""")


def lista_agenda(nome, data, opc):
    if opc == 1:
        contato = f"{nome};{data}\n"
        lista.append(contato)
        lista.sort()  # ordena a lista em ordem alfabética

    elif opc == 2:
        print("=" * 30)
        if not lista:
            print("Lista vazia!\n")
        else:
            removido = lista.pop(0)  # remove o elemento de índice 0
            print(f"Removido: {removido.strip()}")
        print("=" * 30)

    elif opc == 3:
        print("=" * 30)
        if not lista:
            print("Lista vazia!")
        else:
            print("Nome | Data")
            for i in lista:
                print(i.strip())
        print("=" * 30)

    elif opc == 4:
        with open("agenda.csv", "w", encoding="utf-8") as arq:
            arq.writelines(lista)


#------------------------------------------------------------------------------#
# Função principal

opc = 0

while opc != 4:
    menu()

    while True:
        try:
            opc = int(input(": "))
            break
        except ValueError:
            print("Digite apenas números válidos.")

    if opc == 1:
        nome = input("Informe o nome do contato: ")
        data = input("Informe a data de nascimento: ")
        lista_agenda(nome, data, 1)

    elif opc == 2:
        lista_agenda(0, 0, 2)

    elif opc == 3:
        print("Lista de contatos:")
        lista_agenda(0, 0, 3)

    elif opc != 4:
        print("Opção inválida! Escolha entre 1 e 4.")

lista_agenda(0, 0, 4)  # grava a lista na agenda
print("FIM DO PROGRAMA!")