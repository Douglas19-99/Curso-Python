while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*): ')
  
 
 #checando se o usuário digitou numero valido.
    try:
        num1 = float(numero1)
        num2 = float(numero2)

    except ValueError:
        print('Valor digitado inválido.')
        continue

# Checando se o operador é válido.

    operadores_validos = '+-/*'

    if len(operador) != 1:
        print('Por favor, Digite apenas um operador: ')
    
    elif operador not in operadores_validos:
        print('Operador inválido')
        continue
# Contas

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        if num2 == 0:
            print('Divisão por zero não é permitida.')
            continue

        print(num1 / num2)

    elif operador == '*':
        print(num1 * num2)
    
# sair da calculadora

    sair = input('Deseja sair da calculadora? (s/n) ')
    sair = sair.lower().startswith('s')
    if sair:
        print('Vocês saiu')
        break

