class Conta():
    
    def __init__(self, nome_cliente = ' ', telefone_cliente = 99999999,
    conta = 0, saldo = 0):
        self.nome_cliente = [nome_cliente]
        self.telefone_cliente = telefone_cliente
        self.conta = conta
        self.saldo = saldo


    def consulta_saldo(self, nome):
        if nome in self.nome_cliente:
            print(f'Nome do cliente: {nome}')
            print(f'Saldo da conta do cliente: {self.saldo}')


    def status_conta(self, titular):
        if titular in self.nome_cliente:
            print('*' * 50)
            print(f'Titular da conta: {titular}')
            print(f'Contato do titular: {self.telefone_cliente}')
            print(f'Número da conta: {self.conta}')
            print(f'Saldo do cliente: {self.saldo}')
            print('*' * 50)


class Endereco(Conta):
    def __init__(self, morada):
        super().__init__(nome_cliente = ' ', telefone_cliente = 99999999,
        conta = 0, saldo = 0)
        self.morada = morada

    def mudar_endereco(self):
        self.morada = input (f'Digite o novo endereço ')
        return print(f'Endereço atualizado para: {self.morada}')