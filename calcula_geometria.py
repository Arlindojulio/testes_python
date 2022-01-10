from menu_calc_geometria import Menu
from calculador_geometrico import Calculador

Menu()

user = Calculador(int(input('Escolha um número correspondente as opções acima: ')))

if user.opcao == 1:
    user.calc_area_quadrado()
elif user.opcao == 2:
    user.calc_area_retangulo()
elif user.opcao == 3:
    user.calc_area_triagulo()
elif user.opcao == 4:
    user.calc_area_trapezio()
elif user.opcao == 5:
    user.calc_area_circulo()
elif user.opcao == 6:
    user.sair()
else:
    print('ERRO! Você não escolheu uma das opções do MENU.')