'''
Peça ao usuário para digitar o nome completo.
Se for preenchido:

Exiba:

O primeiro nome

O último nome

O número total de palavras no nome
Se estiver vazio:

Mostre: "Campo vazio. Tente novamente."
'''

nome = input ('Digite seu nome completo: ')
# palavras = nome.strip().split() # Coloquei todas essas variaveis dentro dos prints.
# numero_de_palavras = len(palavras)
# primeiro_nome = nome.strip().split()[0]
# ultimo_nome = nome.strip().split()[-1]


if nome:
    print(f'O seu primeiro nome é {(nome.strip().split()[0])}')
    print(f'O seu ultimo nome é {(nome.strip().split()[-1])}')
    print(f'O número de palavras do seu nome é {len(nome.strip().split())}')

else:
    print('Campo vazio. tente novamente')