"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Qual é seu nome? ')
    print(f'Seu nome {nome}')

    if nome == 'sair':
        break

print('Acabou')