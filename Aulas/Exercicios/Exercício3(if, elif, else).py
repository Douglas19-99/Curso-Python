'''
Peça ao usuário para digitar um número inteiro.
Se for um número válido:

Exiba:

O número ao quadrado

Se ele é par ou ímpar

Quantos dígitos ele tem
Se não for válido:

Mostre: "Número inválido."
'''

numero = int(input('Por favor, digite um numero inteiro: '))

if numero > 0:
    quadrado = numero ** 2
    print(f'O numero {numero} ao quadrado é {quadrado}.')
    print(f'Seu numero tem {len(str(abs(numero)))} dígitos.')
    
    if numero % 2 == 0:
        print(f'Seu numero {numero} é par.')
    else:
        print(f'Seu numero {numero} é impar.')

else:
    print('Número inválido!')
