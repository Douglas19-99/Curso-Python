# Exercício 1: Adivinhe o Número

# 1. Preparação: Defina o número secreto.
#    Você pode mudar este número para jogar com um valor diferente!
numero_secreto = 42
palpite = 0 # Inicializa a variável 'palpite' com um valor que não seja o secreto.

print("--- Jogo de Adivinhar o Número ---")
print("Eu pensei em um número entre 1 e 100. Tente adivinhar qual é!")
print("-" * 35)

# 2. Laço Principal: Continua enquanto o palpite do usuário for diferente do número secreto.
#    A condição 'palpite != numero_secreto' significa "palpite NÃO é igual a numero_secreto".
while palpite != numero_secreto:
    # 3. Lógica Interna: Peça um palpite e dê dicas.
    try:
        # Pede ao usuário para digitar um palpite
        palpite_str = input("Qual é o seu palpite? ")
        palpite = int(palpite_str) # Converte a entrada para um número inteiro

        # Compara o palpite com o número secreto
        if palpite < numero_secreto:
            # Se o palpite for menor, dê a dica.
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            # Se o palpite for maior, dê a dica.
            print("Muito alto! Tente um número menor.")
        # Se não for nem menor nem maior, só pode ser igual!
        # Nesse caso, o laço 'while' vai parar na próxima verificação.

    except ValueError:
        # Se o usuário digitar algo que não é um número, informe o erro e continue o laço.
        print("Entrada inválida. Por favor, digite apenas números.")

# 4. Fim do Jogo: Esta linha só é executada quando o laço 'while' termina.
#    Isso acontece quando o usuário acerta o número.
print("-" * 35)
print(f"🎉 Parabéns! Você acertou! O número secreto era {numero_secreto}.")