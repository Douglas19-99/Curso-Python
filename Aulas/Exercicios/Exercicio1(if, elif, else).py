"""
Peça ao usuário para digitar uma palavra.
Se a palavra for digitada:

Mostre:

A palavra digitada

A palavra ao contrário

Quantas letras tem

Se a palavra é toda maiúscula ou minúscula
Se não for digitado nada:

Mostre: "Você não digitou nenhuma palavra."
"""

palavra = input('Digite uma palavra: ')

if palavra:
    print(palavra)
    print(f'Sua palavra ao contrário é {palavra[::-1]}')
    print(f'A sua palavra tem {len(palavra)}')
else:
    print('Você não digitou nenhuma palavra')
