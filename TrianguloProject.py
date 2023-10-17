# Arquivo projeto triangulo

print('\n\t\t\t -- Identificador de Triângulos ')

ladoA = int(input('Digite o lado A: '))
ladoB = int(input('Digite o lado B: '))
ladoC = int(input('Digite o lado C: '))

# Processamento e saída

if ladoA < (ladoB + ladoC) and ladoB < (ladoA + ladoC) and ladoC < (ladoA + ladoB):
    print(f'\nOs lados {ladoA},{ladoB} e {ladoC} formam um triângulo')
    if ladoA == ladoB == ladoC:
        print('Classificação: Triângulo equilátero (possui os 3 lados iguais)')
    elif ladoA != ladoB != ladoC:
        print('Classificação: Triângulo escaleno (possui os 3 lados diferentes)')
    else:
        print('Classificação: Triângulo isósceles (possui 2 lados de mesma medida)')
else:
    print(f'as medidas {ladoA}, {ladoB} e {ladoC} não formam um triângulo')

#testeeeee
