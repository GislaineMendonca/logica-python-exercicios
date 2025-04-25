# Calcule a soma de todos os números de 1 até N.

# Lê o valor de N
n = int(input("Digite um número N: "))

# Calcula a soma de 1 até N
soma = 0
for i in range(1, n + 1):
    soma += i

# Mostra o resultado
print(f"A soma de todos os números de 1 até {n} é {soma}.")
