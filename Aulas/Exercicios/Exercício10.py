'''
<<<<<<< HEAD
Peça dois números ao usuário e diga qual é o maior, ou se são iguais.
Se o usuário não digitar números válidos, exiba uma mensagem de erro.
'''

entrada1 = input('Primeiro número: ')
entrada2 = input('Segundo número: ')

try:
    num1 = float(entrada1)
    num2 = float(entrada2)

    if num1 > num2:
        print('O primeiro número é maior.')
    elif num2 > num1:
        print('O segundo número é maior.')
    else:
        print('Os dois números são iguais.')

except:
    print('Erro: você não digitou números válidos.')

'''
Peça ao usuário uma letra.
Informe se é uma vogal, uma consoante ou uma entrada inválida 
(se não for uma única letra do alfabeto).
'''

letra = input('Digite uma letra: ')


if len(letra) == 1 and letra.isalpha(): # garante que o usuário digitou apenas uma letra.
    letra = letra.lower() # Converte para minúscula com lower() para facilitar a comparação.
    if letra in 'aeiou':
        print('A letra digitada é uma vogal.')

    else:
        print('A letra digitada é uma consoante.')

else:
    print('entrada inválida')

'''
Peça ao usuário um número. Informe:
Se é divisível por 3 e 5
Se é divisível apenas por 3
Se é divisível apenas por 5
Se não é divisível por nenhum dos dois
Caso a entrada não seja um número válido, exiba erro.
'''


numero = input('Informe um número: ')

if numero.lstrip('-').isdigit(): # lstrip('')  remove o sinal de menos - da esquerda da string,
 #se existir assim ele permite numero inteiro negativos
    num = int(numero)
    
    if num % 3 == 0 and num % 5 == 0:
        print('Seu número é divisível por 3 e 5.')
    elif num % 3 == 0:
        print('Seu número é divisível apenas por 3.')
    elif num % 5 == 0:
        print('Seu número é divisível apenas por 5.')

    else:
        print('Seu número não é divisível por nenhum dos dois.')

else:
    print('Número inválido. tente novamente.')

'''
Peça o ano de nascimento do usuário e calcule a idade.
Com base nisso, diga se ele é maior de idade (18 anos ou mais) ou menor de idade.
Considere o ano atual como 2025 (ou use datetime se quiser evoluir o código).
'''
from datetime import date

ano_nascimento = int(input('Digite sua idade: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

    
if idade >= 18:
    print(f'Você nasceu em {idade} e é maior de idade.')
else:
    print(f'Você nasceu em {idade} e é menor de idade.')

=======
Peça ao usuário para digitar um número.
Informe se o número é positivo, 
negativo ou igual a zero.
Caso o usuário não digite um número válido, informe que a entrada é inválida.
'''

# numero = int(input('Digite um número: '))


# try:
#     positivo = numero > 0
#     negativo = numero < 0

#     if positivo:
#         print('Seu número é positivo.')
#     elif negativo:
#         print('Seu número é negativo')
#     else:
#         print('Seu número é zero.')

# except:
#     print('Entrada inválida')

'''
Peça ao usuário para digitar um ano.
Informe se o ano é bissexto ou não.
(Dica: anos bissextos são divisíveis por 4, mas não por 100, exceto se também forem divisíveis por 400.)
'''

# ano = input('Digite um Ano:')

# if ano.isdigit:  Para usar .isdigit como numero inteiro tem que transformar ele dentro do código.
#     ano = int(ano)
#     if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#         print('O ano digitado é bissexto.')
#     else:
#         print('O ano digitado não é bissexto')
# else:
#     print('Ano inválido.')

'''
Peça a idade do usuário e classifique da seguinte forma:
Até 12 anos: Criança
De 13 a 17 anos: Adolescente
De 18 a 59 anos: Adulto
60 anos ou mais: Idoso

'''
# entrada = input('Digite sua idade: ')

# if entrada.isdigit():
#     entrada = int(entrada)
#     if entrada <= 12:
#         print('Você é uma criança.')
#     elif entrada > 12 and entrada <= 17:
#         print('Você é uma adolescente.')
#     elif entrada >= 18 and entrada <= 59:
#         print('Você é um adulto')
#     else:
#         print('Você é idoso.')
# else:
#     print('Valor inválido, tente novamente.')

'''

Verificar tamanho de uma palavra
Peça ao usuário para digitar uma palavra. Diga quantas letras tem a palavra e classifique o tamanho:

Menor que 4 letras: Muito curta

Entre 4 e 7 letras: Curta

Entre 8 e 11 letras: Média

12 letras ou mais: Longa

'''

# entrada = input('Digite uma palavra: ')


# if entrada.isalpha():
#     tamanho = len(entrada)
#     print(f'A palavra tem {tamanho} letras.')
    
#     if tamanho < 4:
#         print('Palavra digitada é muito curta.')
#     elif tamanho >= 4 and tamanho <= 7:
#         print('Palavra digitada é curta.')
#     elif tamanho >= 8 and tamanho <= 11:
#         print('Palavra digtitada é média.')
#     else:
#         print('Palavra digitada é longa')

# else:
#     print('Entrada inválida. Digite apenas letras.')
>>>>>>> c599777b54df6f8067c3345dd9ae1371c00ecc9f
