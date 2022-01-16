from classe_conta_bancaria import Conta
from classe_conta_bancaria import Endereco

conta1 = Conta('Arlindo')
conta1.consulta_saldo('Arlindo')

conta2 = Conta('Ana', 987369159, 2, 5000)
conta2.consulta_saldo('Ana')

conta3 = Conta('José', 987363259, 3, )
conta3.status_conta('José')

conta1 = Endereco('Vila do Conde')
conta1.mudar_endereco()