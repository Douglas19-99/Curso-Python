'''
<<<<<<< HEAD
Escreva um programa que pede a idade do usuário e
diz se ele pode tirar a carteira de motorista (precisa ter 18 anos ou mais).
'''
idade = input('Digite sua idade: ')

if idade.isdigit():
    num = int(idade)

    if num >= 18:
        print('Você pode tirar a carteira de motorista.')

    else:
        print('Você não pode tirar a carteira de mostorista.')

else:
    print('Valor inválido. Tente novamente.')

'''
Peça um número inteiro e diga se ele é par ou ímpar.
'''

entrada = input('Digite um número inteiro: ')

try:
    num = int(entrada)
    if num % 2 == 0:
        print('O número é par.')

    else:
        print('O número é impar.')

except ValueError:
    print('Entrada inválida. Tente novamente.')

'''
Crie uma variável nome e verifique se ela está vazia.
Se estiver, exiba "Nome não informado".
'''
#if nome.strip() == "" verifica se a string está vazia depois de limpar os espaços.
#nome.strip() remove espaços em branco no início e no fim da string.

nome = input("Digite seu nome: ")
        
if nome.strip() == "": 
    print("Nome não informado.")
else:
    print(f"Olá, {nome}!")
=======
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

>>>>>>> c599777b54df6f8067c3345dd9ae1371c00ecc9f
