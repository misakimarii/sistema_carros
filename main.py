# main.py
import os
import json
from models.carro import Carro

def apagar_carros():
    caminho_arquivo = "carros.json"
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
        print("Todos os carros foram apagados com sucesso! ")
    else: 
        print("Nenhum carro encontrado para apagar")

def menu():
    print("\n=== SISTEMA DE CADASTRO DE CARROS ===")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Apagar todos os carros")
    print("0 - Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        print("\n--- CADASTRAR CARRO ---")
        
        escolha_marca = input("Escolha a marca: \n1 - Fiat\n2 - Volkswagen\n3 - Chevrolet\n4 - BMW\n5 - Porsche\nOpção: ")
        
        if escolha_marca == "1":
            marca = "Fiat"
            escolha_modelo = input("Escolha o modelo:\n1 - Uno\n2 - Argo\n3 - Mobi\nOpção: ")

            if escolha_modelo == "1":
                modelo = "Uno"
            elif escolha_modelo == "2":
                modelo = "Argo"
            elif escolha_modelo == "3":
                modelo = "Mobi"
            else:
                print("Modelo desconhecido, digite um valor válido")
                modelo = "Desconhecido"

        elif escolha_marca == "2":
            marca = "Volkswagen"
            escolha_modelo = input("Escolha o modelo:\n1 - Gol\n2 - Polo\n3 - T-Cross\nOpção: ")
            
            if escolha_modelo == "1":
                modelo = "Gol"
            elif escolha_modelo == "2":
                modelo = "Polo"
            elif escolha_modelo == "3":
                modelo = "T-Cross"
            else:
                print("Modelo desconhecido, digite um valor válido")
                modelo = "Desconhecido"

        elif escolha_marca == "3":
            marca = "Chevrolet"
            escolha_modelo = input("Escolha o modelo:\n1 - Onix\n2 - Prisma\n3 - Tracker\nOpção: ")

            if escolha_modelo == "1":
                modelo = "Onix"
            elif escolha_modelo == "2":
                modelo = "Prisma"
            elif escolha_modelo == "3":
                modelo = "Tracker"
            else:
                print("Modelo desconhecido, digite um valor válido")
                modelo = "Desconhecido"

        elif escolha_marca == "4":
            marca = "BMW"
            escolha_modelo = input("Escolha o modelo:\n1 - 320i\n2 - X1\n3 - M5\nOpção: ")

            if escolha_modelo == "1":
                modelo = "320i"
            elif escolha_modelo == "2":
                modelo = "X1"
            elif escolha_modelo == "3":
                modelo = "M5"
            else:
                print("Modelo desconhecido, digite um valor válido")
                modelo = "Desconhecido"

        elif escolha_marca == "5":
            marca = "Porsche"
            escolha_modelo = input("Escolha o modelo:\n1 - 911\n2 - Cayman\n3 - Panamera\nOpção: ")

            if escolha_modelo == "1":
                modelo = "911"
            elif escolha_modelo == "2":
                modelo = "Cayman"
            elif escolha_modelo == "3":
                modelo = "Panamera"
            else:
                modelo = "Desconhecido"

        else:
            print("Opção inválida! Marca definida como 'Desconhecida'.")
            marca = "Desconhecida"
            modelo = "Desconhecido"

        
        ano = input("Ano: ")
        while not ano.isdigit():
            print("Ano inválido! Digite apenas números.")
            ano = input("Ano: ")

        carro = Carro(marca, modelo, ano)
        carro.salvar_carro()

        print("Carro salvo com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE CARROS ---")

        lista = Carro("", "", "").carregar_dados()

        if not lista:
            print("Nenhum carro cadastrado, adicione um carro antes de conferir a lista.")
        else:
            for c in lista:
                print(f"{c['marca']} - {c['modelo']} - {c['ano']}")

    elif opcao == "3":
        apagar_carros()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!")

