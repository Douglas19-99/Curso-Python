'''
Peça ao usuário para digitar uma frase.
Se digitada corretamente:

Exiba:

A frase em letras maiúsculas

A frase em letras minúsculas

Quantas palavras ela tem

Quantas vezes aparece a letra "a"
Se não for digitado nada:

Mostre: "Frase vazia. Tente novamente."
'''

frase = input('Por favor, digite uma frase: ')
letra = 'a'
if frase:
    print(f'Sua frase em letras maiúsculas {frase.upper()}')
    print(f'Sua frase em letras minúsculas {frase.lower()}')
    print(f'Quantas vezes aparece a letra A na sua frase: {frase.count(letra)}')


else:
    print('Frase vazia. Tene novamente.')
    