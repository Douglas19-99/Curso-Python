'''
Peça dois números ao usuário e diga qual é o maior, ou se são iguais.
Se o usuário não digitar números válidos, exiba uma mensagem de erro.
'''

# entrada1 = input('Primeiro número: ')
# entrada2 = input('Segundo número: ')

# try:
#     num1 = float(entrada1)
#     num2 = float(entrada2)

#     if num1 > num2:
#         print('O primeiro número é maior.')
#     elif num2 > num1:
#         print('O segundo número é maior.')
#     else:
#         print('Os dois números são iguais.')

# except:
#     print('Erro: você não digitou números válidos.')

'''
Peça ao usuário uma letra.
Informe se é uma vogal, uma consoante ou uma entrada inválida 
(se não for uma única letra do alfabeto).
'''

# letra = input('Digite uma letra: ')


# if len(letra) == 1 and letra.isalpha(): # garante que o usuário digitou apenas uma letra.
#     letra = letra.lower() # Converte para minúscula com lower() para facilitar a comparação.
#     if letra in 'aeiou':
#         print('A letra digitada é uma vogal.')

#     else:
#         print('A letra digitada é uma consoante.')

# else:
#     print('entrada inválida')

'''
Peça ao usuário um número. Informe:
Se é divisível por 3 e 5
Se é divisível apenas por 3
Se é divisível apenas por 5
Se não é divisível por nenhum dos dois
Caso a entrada não seja um número válido, exiba erro.
'''


# numero = input('Informe um número: ')

# if numero.lstrip('-').isdigit(): # lstrip('')  remove o sinal de menos - da esquerda da string,
#  se existir assim ele permite numero inteiro negativos
#     num = int(numero)
    
#     if num % 3 == 0 and num % 5 == 0:
#         print('Seu número é divisível por 3 e 5.')
#     elif num % 3 == 0:
#         print('Seu número é divisível apenas por 3.')
#     elif num % 5 == 0:
#         print('Seu número é divisível apenas por 5.')

#     else:
#         print('Seu número não é divisível por nenhum dos dois.')

# else:
#     print('Número inválido. tente novamente.')

'''
Peça o ano de nascimento do usuário e calcule a idade.
Com base nisso, diga se ele é maior de idade (18 anos ou mais) ou menor de idade.
Considere o ano atual como 2025 (ou use datetime se quiser evoluir o código).
'''
# from datetime import date

# ano_nascimento = int(input('Digite sua idade: '))
# ano_atual = date.today().year
# idade = ano_atual - ano_nascimento

    
# if idade >= 18:
#     print(f'Você nasceu em {idade} e é maior de idade.')
# else:
#     print(f'Você nasceu em {idade} e é menor de idade.')

