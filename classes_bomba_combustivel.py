from menu_posto_combustivel import MenuPostoCombustivel

class BombaCombustivel():
    def __init__(self, tipo_combustivel, valor_litro, quant_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quant_combustivel = quant_combustivel
        #valor_abastecimento = 0


    def abastecer_litros(self, quantidade_litro : int):
        self.quant_combustivel -= quantidade_litro
        valor_abastecimento = self.valor_litro * quantidade_litro
        print('*' * 80)
        print(f'Abastecimento de {quantidade_litro} litros de {self.tipo_combustivel} realizado.')
        print(f'Valor total do abastecimento:R$ {valor_abastecimento: .2f}')
        print('*' * 80)


    def abastecer_valor(self, valor):
        quant_abastecido = valor / self.valor_litro
        self.quant_combustivel = self.quant_combustivel - quant_abastecido
        print('*' * 80)
        print(f'Abastecimento de {quant_abastecido: .2f} litros de {self.tipo_combustivel} realizado.')
        print(f'Valor total do abastecimento:R$ {valor: .2f}')
        print('*' * 80)


    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        print('*' * 80)
        print(f'O valor do combustível {self.tipo_combustivel} foi alterado.')
        print(f'Novo valor do/a {self.tipo_combustivel}:R$ {self.valor_litro}')


    def set_aterar_combustivel(self, combustivel):
        self.tipo_combustivel = combustivel
        return print(f'Combustivel alterado para {self.tipo_combustivel}')


    def get_status_bomba(self):
        print(' ')
        print(f'#' * 30 + ' Status da Bomba ' + '#' * 30)
        print(f'Quantidade de combustível na bomba {self.tipo_combustivel}: {self.quant_combustivel: .2f} litros')
        print(f'#' * 90)
