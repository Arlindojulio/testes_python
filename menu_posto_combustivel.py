class MenuPostoCombustivel():
    def __init__(self):
        self.escolha = {
                1 : 'diesel',
                2 : 'gasolina',
                3 : 'alcóol',
                4 : 'sair'
        }


    def get_escolha(self):
        return self.escolha


    def get_menu(self):
        print(f'#' * 80)
        print(f' ' * 30 + 'Bem vindo ao posto Brazuca')
        print(' '* 10 + f'Selecione uma operação de abastecimento:')
        print(' ')
        print(' '* 10 +  f'{self.escolha.get(1)} = 1 ' + ' '* 20 + f'{self.escolha.get(2)} = 2')
        print(' '* 10 +  f'{self.escolha.get(3)} = 3 ' + ' '* 20 + f'{self.escolha.get(4)} = 4')
        print(f'#' * 80)


    def litro_valor(self):
        print(f'#' * 80)
        print(f'Abastecer por litros = 1        Abastecer por valor = 2')
        print(f'#' * 80)