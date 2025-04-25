# O programa escolhe um número aleatório e o usuário tem que adivinhar.

import random

numero_secreto = random.randint(1, 100)
tentativa = -1

print("Tente adivinhar o número entre 1 e 100!")

while tentativa != numero_secreto:
    tentativa = int(input("Digite sua tentativa: "))
    
    if tentativa < numero_secreto:
        print("Muito baixo. Tente novamente.")
    elif tentativa > numero_secreto:
        print("Muito alto. Tente novamente.")
    else:
        print("Parabéns! Você acertou!")