# Exercício 2: Somador de Números

# 1. Inicialização: Comece com a soma total igual a zero.
soma_total = 0

print("--- Somador de Números ---")
print("Digite vários números para somar. Digite 0 para sair e ver o resultado.")
print("-" * 60)

# 2. Laço Infinito: 'while True' cria um laço que só para com um 'break'.
while True:
    try:
        # Pede um número ao usuário dentro do laço
        numero_str = input("Digite um número (ou 0 para parar): ")
        numero = float(numero_str)  # Converte para float para aceitar números decimais

        # 3. Condição de Parada: Verifica se o número é o 'sinal' para parar.
        if numero == 0:
            break  # Interrompe o laço 'while' imediatamente.

        # 4. Acumulação: Adiciona o número à soma total.
        soma_total = soma_total + numero  # ou a forma mais curta: soma_total += numero

    except ValueError:
        # Se o usuário digitar algo que não seja um número, avise-o.
        print("Entrada inválida. Por favor, digite apenas números.")

# 5. Resultado Final: Esta linha é executada após o 'break' do laço.
print("-" * 60)
print(f"A soma total dos números digitados é: {soma_total}")
