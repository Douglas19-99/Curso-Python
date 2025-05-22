'''
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