'''
Peça uma palavra ao usuário.
Se a palavra for válida:

Mostre:

A primeira letra

A última letra

Se começa com vogal ou consoante
Se não for:

Mostre: "Digite uma palavra válida."
'''

palavra = input('Digite uma palavra: ')

if palavra:
    print(f'A primeira letra da palavra é {palavra[0]}')
    print(f'A última letra da sua palavra é {palavra[-1]}')
    
    if palavra.strip().lower()[0] in 'aeiou':
        print('Começa com vogal.')
    
    else:
        print('Começa com consoante.')

else:
    print('Digite uma palavra válida.')