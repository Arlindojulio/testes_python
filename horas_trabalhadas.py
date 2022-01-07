dias = {
    'domingo' : int(input('Quantas horas você trabalhou no domingo? ')),
    'Segunda' : int(input('Quantas horas você trabalhou na segunda feira? ')),
    'terca' : int(input('Quantas horas você trabalhou na terça feira? ')),
    'quarta' : int(input('Quantas horas você trabalhou no quarta feira? ')),
    'quinta' : int(input('Quantas horas você trabalhou na quinta feira? ')),
    'sexta' : int(input('Quantas horas você trabalhou na sexta feira? ')),
    'sabado' : int(input('Quantas horas você trabalhou no sábado? '))
}

num_horas = 0
soma_horas = 0
dia = ''
horas_extra = 10

for dias_trabalhados, quant_horas in dias.items():
    if horas_extra >= quant_horas:
        if num_horas < quant_horas:
            num_horas = quant_horas
            dia = dias_trabalhados
        soma_horas += quant_horas
    else:
        excesso = dias_trabalhados
        print (f'ERRO!! O valor digitado no dia {excesso} foi desconsiderado por está fora do permitido por lei.')
        break
   
print(f'Essa semana você trabalhou no total {soma_horas} horas.')
print(f'O dia que você trabalhou mais horas foi {dia}, quando você trabalhou {num_horas} horas.')