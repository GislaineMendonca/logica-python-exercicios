#Implemente uma mini calculadora que interpreta expressões do tipo 3 + 4 * 2.

def mini_calculadora(expressao):
    # Remove espaços em branco
    expressao = expressao.replace(' ', '')
    
    # Lista para armazenar os tokens (números e operadores)
    tokens = []
    i = 0
    while i < len(expressao):
        if expressao[i] in '+-*/':
            tokens.append(expressao[i])
            i += 1
        else:
            # Coletar número (pode ter múltiplos dígitos)
            num_str = ''
            while i < len(expressao) and expressao[i].isdigit():
                num_str += expressao[i]
                i += 1
            if num_str:
                tokens.append(int(num_str))
    
    # Primeira passada: processar * e /
    i = 0
    while i < len(tokens) - 1:
        token = tokens[i]
        if token == '*' or token == '/':
            # Encontrou operador de alta precedência
            num1 = tokens[i-1]
            op = tokens[i]
            num2 = tokens[i+1]
            
            # Realiza a operação
            if op == '*':
                resultado = num1 * num2
            else:
                resultado = num1 // num2  # Divisão inteira
            
            # Substitui os 3 elementos pelo resultado
            tokens[i-1:i+2] = [resultado]
            # Não incrementa i pois o array foi reduzido
        else:
            i += 1
    
    # Segunda passada: processar + e -
    resultado = tokens[0]
    i = 1
    while i < len(tokens):
        op = tokens[i]
        num = tokens[i+1]
        if op == '+':
            resultado += num
        else:
            resultado -= num
        i += 2
    
    return resultado

# Testes
print(mini_calculadora("3 + 4 * 2"))  # 11
print(mini_calculadora("10 - 5 * 2"))  # 0
print(mini_calculadora("8 / 2 + 3"))  # 7
print(mini_calculadora("10 + 20 + 30"))  # 60
print(mini_calculadora("10 * 2 * 3"))  # 60
print(mini_calculadora("10 - 2 - 3"))  # 5