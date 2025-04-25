# Mostre a tabuada de um número informado pelo usuário.

# Lê o número do usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Mostra a tabuada do número
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")