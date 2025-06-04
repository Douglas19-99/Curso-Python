'''
Objetivo: Crie um programa que peça a idade do usuário e,
em seguida, classifique e imprima a faixa etária correspondente:

0-12 anos: Criança
13-17 anos: Adolescente
18-59 anos: Adulto
60 anos ou mais: Idoso
'''

entrada = input('Digite sua idade: ')


if entrada.isdigit():
    num = int(entrada)

    if num >= 0 and num <= 12:
        print('Você tem', entrada, 'anos, você é uma criança.')
    if num >= 13 and num <= 17:
        print('Você tem', entrada, 'anos, você  é um adolescente.')
    elif num >= 18 and num <= 59:
        print('Você tem', entrada, 'anos, você  é um adulto.')
    else:
        print('Você tem', entrada, 'anos, você  é um idoso.')

else:
    print('valor digitado inválido. Tente novamente.')


