# main.py

from models.carro import Carro

def menu():
    print("\n=== SISTEMA DE CADASTRO DE CARROS ===")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("0 - Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        print("\n--- CADASTRAR CARRO ---")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")

        carro = Carro(marca, modelo, ano)
        carro.salvar_carro()

        print("Carro salvo com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE CARROS ---")

        lista = Carro("", "", "").carregar_dados()

        if not lista:
            print("Nenhum carro cadastrado ainda.")
        else:
            for c in lista:
                print(f"{c['marca']} - {c['modelo']} - {c['ano']}")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

