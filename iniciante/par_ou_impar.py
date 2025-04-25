# Escreva um programa que leia um número e diga se ele é par ou ímpar.

# Lê um número do usuário
numero = float(input("Digite um número: "))

# Verifica se é par ou ímpar
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")