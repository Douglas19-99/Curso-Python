entrada = input('Insira um numero de 1 a 7: ')

try:   
    numero = int(entrada)

    if numero <= 0 or numero > 7:
        print('Número inválido. Digite um numero inteiro de 1 a 7.')
    
    elif numero == 1:
        print('Você digitou 1, ele corresponde a Domingo.')
    elif numero == 2:
        print('Você digitou 2, ele corresponde a Segunda-feira.')
    elif numero == 3:
        print('Você digitou 3, ele corresponde a terça-feira.')
    elif numero == 4:
        print('Você digitou 4, ele corresponde a Quarta-feira.')
    elif numero == 5:
        print('Você digitou 5, ele corresponde a Quinta-feira.')
    elif numero == 6:
        print('Você digitou 6, ele corresponde a Sexta-feira .')
    else:
        print('Você digitou 7, ele corresponde a Sábado.')
except ValueError:
    print('Entrada inválida, tente novamente.')