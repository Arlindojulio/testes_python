nome_completo = str([input('Digite seu nome completo: ')])
nome_completo = nome_completo.split() #função para transformar o nome digitado pelo usuário em uma lista
nome_sigla = [nome_completo[0]] #lista para guardar o 1º nome e a 1ª letras dos sobrenomes

'''
for nome in nome_completo: #ciclo for para percorrer a lista com o nome digitado
    if nome == ' ': #condicional para captar a 1ª letra do sobrenome (uso do ' '(espaço como referência))
        sepador = nome_completo.index(nome) + 1 #a variável separador guarda a posição da letra seguinte ao espaço
        nome_sigla.append(nome_completo[2 : sepador])#o 1º nome digitado antes do espaço é adcionado a lista (nome_sigla)
        nome_sigla += nome_completo[sepador] #a 1ª letra depois do espaço ' ' é adicionada a lista (nome_sigla)
        
        print(sepador) #mostra quanto tá valendo a variável separador
        print(nome_sigla) #mostra o conteúdo da lista nome_sigla
        print(nome_completo) #mostra o conteúdo da lista nome_completo
'''
contador = 0
for nome in nome_completo:
    if nome not in nome_sigla:
        nome_sigla.append(nome_completo[contador])
    contador += 1

print(nome_sigla)