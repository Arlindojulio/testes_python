nome_completo = str([input('Digite seu nome completo: ')])
nome_sigla = [] #lista para guardar o 1º nome e a 1ª letras dos sobrenomes

nome_completo.split() #função para transformar o nome digitado pelo usuário em uma lista

for nome in nome_completo: #ciclo for para percorrer a lista com o nome digitado
    if nome == ' ': #condicional para captar a 1ª letra do sobrenome (uso do ' '(espaço como referência))
        sepador = nome_completo.index(nome) + 1 #a variável separador guarda a posição da letra seguinte ao espaço
        nome_sigla.append(nome_completo[2 : sepador])#o 1º nome digitado antes do espaço é adcionado a lista (nome_sigla)
        nome_sigla += nome_completo[sepador] #a 1ª letra depois do espaço ' ' é adicionada a lista (nome_sigla)
        
        print(sepador) #mostra quanto tá valendo a variável separador
        print(nome_sigla) #mostra o conteúdo da lista nome_sigla
        print(nome_completo) #mostra o conteúdo da lista nome_completo
    