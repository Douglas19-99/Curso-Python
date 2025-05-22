'''
Calculadora com while
'''

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None
    try:
        num_1_float = float(numero_1)
        num_2_floar = float(numero_2)
        numeros_validos = True
    except Exception:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitiros = '+-/*'

    if operador not in operadores_permitiros:
        print('Operador inválido. ')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if 

    

    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
