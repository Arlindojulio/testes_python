from menu_calc_geometria import Menu
from calculador_geometrico import Calculador

Menu()

user = Calculador(int(input('Escolha um número correspondente as opções acima: ')))

if user.opcao == 1:
    user.calc_area_quadrado()
elif user.opcao == 2:
    user.calc_area_triagulo()