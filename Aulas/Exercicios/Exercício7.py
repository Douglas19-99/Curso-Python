'''
Peça ao usuário para digitar seu nome e uma frase qualquer.

Se os dois forem preenchidos:

Mostre:

O nome com a primeira letra de cada palavra maiúscula (title())

Quantas vezes o nome aparece na frase (ignore maiúsculas/minúsculas)

A frase invertida

Diga se a frase termina com ponto final .
Caso contrário:

Mostre: "Campos vazios. Tente novamente."
'''
nome = input('Digite seu nome: ')
frase = input('Digite uma frase: ')

if nome and frase:
    # Nome com a primeira letra de cada palavra maiúscula
    nome_formatado = nome.title()
    
    # Contagem do nome na frase (ignorando maiúsculas/minúsculas)
    contagem_nome = frase.lower().count(nome.lower())
    
    # Frase invertida
    frase_invertida = frase[::-1]
    
    # Verifica se termina com ponto final
    termina_com_ponto = frase.strip().endswith('.')
    
    print(f"Nome formatado: {nome_formatado}")
    print(f"O nome aparece {contagem_nome} vez(es) na frase.")
    print(f"Frase invertida: {frase_invertida}")
    
    if termina_com_ponto:
        print("A frase termina com ponto final.")
    else:
        print("A frase NÃO termina com ponto final.")
else:
    print("Campos vazios. Tente novamente.")
    
