class Conta():
    
    def __init__(self, nome_cliente, telefone_cliente, conta, saldo):
        self.nome_cliente = nome_cliente
        self.telefone_cliente = telefone_cliente
        self.conta = conta
        self.saldo = saldo


    def consulta_saldo(self, nome):
        print(f'Nome do cliente: {nome}')
        print(f'Saldo da conta do cliente: {self.saldo}')
        