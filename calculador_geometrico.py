class Calculador:

    def __init__(self, opcao):
        self.opcao = opcao


    def calc_area_quadrado(self):
        lado = float(input('Digite o valor(cm) correspondente aos LADOS do quadrado: '))
        area_quadrado = lado ** 2
        print(f'A área total do quadrado é {area_quadrado}cm2.')


    def calc_area_triagulo(self):
        base = float(input('Digite o valor(cm) correspondente a base do triângulo: '))
        altura = float(input('Digite o valor(cm) correspondente a altura do triângulo: '))
        area_triangulo = (base * altura) / 2
        print(f'A área total do triângulo é {area_triangulo}cm2.')
