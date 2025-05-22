'''
Peça ao usuário uma palavra.
Se for digitada corretamente:

Mostre:

Quantas letras tem

Quantas são vogais

Quantas são consoantes

Se a palavra começa e termina com a mesma letra
Se não for digitado nada:

Mostre: "Nenhuma palavra foi digitada."
'''

palavra = input('Digite um palavra: ')
vogais = 'aeiouAEIOU'
vogais = "aeiouAEIOU"
qtd_vogais = 0
qtd_consoantes = 0
mesma_letra = palavra[0].lower() == palavra[-1].lower()

if palavra:
    for letra in palavra:
        if letra.isalpha():
            if letra in vogais:
                qtd_vogais += 1
            else:
                qtd_consoantes += 1
    
    
    print(f'A palavra digitada tem {len(palavra)} letras.')
    print(f'Quantidade de vogais {qtd_vogais}')
    print(f'Quantidade de consoantes {qtd_consoantes}')


    if mesma_letra :
        print('A palavra começa e termina com a mesma letra.')
        
        

    else:
         print('A palavra NÃO começa e termina com a mesma letra.')


else:
    print('Nenhuma palavra foi digitada.')