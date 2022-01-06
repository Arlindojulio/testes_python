nome_completo = str([input('Digite seu nome completo: ')])
nome_completo = nome_completo.split() #função para transformar o nome digitado pelo usuário em uma lista
nome_sigla = [nome_completo[0]] #lista para guardar o 1º nome e a 1ª letras dos sobrenomes
lista_exclusao = ['de', 'da', 'do', 'dos'] #lista com nomes que não podem aparecer na silga

for nome in nome_completo:
    if nome not in nome_sigla:
        if nome in lista_exclusao:
            None
        else:
            lista_letras = nome.split()
            for letra in lista_letras:
                nome_sigla.append(letra[0])

concatenacao = ' '
nome_sigla = concatenacao.join(nome_sigla)

print(f'Nome do usuário abreviado: {nome_sigla[2 : ]}')