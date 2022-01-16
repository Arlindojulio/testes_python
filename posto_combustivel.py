from classes_bomba_combustivel import BombaCombustivel
from menu_posto_combustivel import MenuPostoCombustivel

bomba1 = BombaCombustivel('diesel', 1.47, 500)
bomba2 = BombaCombustivel('gasolina', 1.42, 850)
bomba3 = BombaCombustivel('alcóol', 1.07, 760)
cliente = MenuPostoCombustivel()

def escolha_cliente(litro_ou_valor):
    if litro_ou_valor == 1:
        litros = int(input(f'Quantos litros deseja abastecer: '))
        bomba1.abastecer_litros(litros)
    elif litro_ou_valor == 2:
        valor = int(input(f'Qual o valor que deseja abastecer: '))
        bomba1.abastecer_valor(valor)
#escolha = EscolherAbastecimento()
cliente.get_menu()
menu_escolha = int(input())

if menu_escolha in cliente.get_escolha():
    if menu_escolha == 1:
        cliente.litro_valor()
        litro_valor = int(input())
        if litro_valor == 1:
            litros = int(input(f'Quantos litros deseja abastecer: '))
            bomba1.abastecer_litros(litros)
        elif litro_valor == 2:
            valor = int(input(f'Qual o valor que deseja abastecer: '))
            bomba1.abastecer_valor(valor)
    elif menu_escolha == 2:
        cliente.litro_valor()
        litro_valor = int(input())
        if litro_valor == 1:
            litros = int(input(f'Quantos litros deseja abastecer: '))
            bomba2.abastecer_litros(litros)
        elif litro_valor == 2:
            valor = int(input(f'Qual o valor que deseja abastecer: '))
            bomba2.abastecer_valor(valor)
    elif menu_escolha == 3:
        cliente.litro_valor()
        litro_valor = int(input())
        if litro_valor == 1:
            litros = int(input(f'Quantos litros deseja abastecer: '))
            bomba3.abastecer_litros(litros)
        elif litro_valor == 2:
            valor = int(input(f'Qual o valor que deseja abastecer: '))
            bomba3.abastecer_valor(valor)
    else:
        print(' ')
        
bomba1.get_status_bomba()
bomba2.get_status_bomba()
bomba3.get_status_bomba()
