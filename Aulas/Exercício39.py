'''
iterando strings com while
'''

#       012345678910
#nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321

nome = 'Luiz Otávio'

indice = 0 
novo_nome = '' # onde o novo nome com asteriscos será montado.
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)