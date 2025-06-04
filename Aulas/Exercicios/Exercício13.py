'''
Objetivo: Escreva um programa que solicite uma nota (de 0 a 100) e imprima a classificação:

90-100: A
80-89: B
70-79: C
60-69: D
Abaixo de 60: F
Se a nota for inválida (menor que 0 ou maior que 100), imprima "Nota inválida".
'''

try:
    nota_str = input('Digite sua nota (0-100): ')
    nota= float(nota_str) # Usei float para permitir a entrada de notas com casa decimais.
    if nota <0 or nota >100:
        print('Nota inválida. Por favor, insira um valor entre 0 e 100.')
    elif nota >= 90:
        print('Sua nota é A')
    elif nota >= 80:
        print('Sua nota é B')
    elif nota >= 70:
        print('Sua nota é C')
    elif nota >= 60:
        print('Sua nota é D')
    else: 
         print('Sua nota é F')

except ValueError:
    print('Entrada inválida. Por favor, digite um número.')