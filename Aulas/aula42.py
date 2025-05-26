frase = 'O python é uma linguagem de programção '\
'multiparadigma. '\
'Python foi criado por Guido van Rossun'

i = 0
qta_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ' '

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
        

    qta_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qta_apareceu_mais_vezes < qta_apareceu_mais_vezes_atual:
        qta_apareceu_mais_vezes = qta_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

   
    i += 1

print ('A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qta_apareceu_mais_vezes}x')