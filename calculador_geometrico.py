class Calculador:

    def __init__(self, opcao):
        self.opcao = opcao


    def calc_area_quadrado(self):
        lado = float(input('Digite o valor(cm) correspondente aos LADOS do quadrado: '))
        area_quadrado = lado ** 2
        print(f'A área total do quadrado é {area_quadrado}cm2.')


    def calc_area_retangulo(self):
        base = float(input('Digite o valor(cm) correspondente a base do retângulo: '))
        altura = float(input('Digite o valor(cm) correspondente a altura do retângulo: '))
        area_retangulo = base * altura
        print(f'A área total do retangulo é {area_retangulo}cm2.')


    def calc_area_triagulo(self):
        base = float(input('Digite o valor(cm) correspondente a base do triângulo: '))
        altura = float(input('Digite o valor(cm) correspondente a altura do triângulo: '))
        area_triangulo = (base * altura) / 2
        print(f'A área total do triângulo é {area_triangulo}cm2.')


    def calc_area_trapezio(self):
        base1 = float(input('Digite o valor(cm) correspondente a primeira base do trapézio: '))
        base2 = float(input('Digite o valor(cm) correspondente a segunda base do trapézio: '))
        altura = float(input('Digite o valor(cm) correspondente a altura do retângulo: '))
        area_trapezio = ((base1 + base2) / 2) * altura
        print(f'A área total do trapézio é {area_trapezio}cm2.')


    def calc_area_circulo(self):
        raio = float(input('Digite o valor(cm) correspondente ao raio do circulo: '))
        area_circulo = (3.14 * (raio ** 2))
        print(f'A área total do circulo é {area_circulo}cm2.')


    def sair(self):
        pass
