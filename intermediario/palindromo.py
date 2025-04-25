# Verifique se uma palavra ou frase é um palíndromo (ignorar espaços e acentuação).

entrada = input("Digite uma palavra ou frase: ")

# Remove espaços e acentos, e coloca tudo em minúsculas
frase = ""
acentos = {
    'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
    'é': 'e', 'ê': 'e',
    'í': 'i',
    'ó': 'o', 'ô': 'o', 'õ': 'o',
    'ú': 'u',
    'ç': 'c'
}

for caractere in entrada.lower():
    if caractere != ' ':
        if caractere in acentos:
            frase += acentos[caractere]
        else:
            frase += caractere

# Verifica se é palíndromo
invertida = ""
i = len(frase) - 1
while i >= 0:
    invertida += frase[i]
    i -= 1

if frase == invertida:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
