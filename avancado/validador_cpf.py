# Implemente uma lógica básica para verificar se um CPF pode ser válido.

def validar_cpf(cpf):
    # Remover caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verificar se todos os números são iguais (exemplo: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return False
    
    # Calcular o primeiro dígito verificador
    soma1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma1 * 10) % 11
    if digito1 == 10:
        digito1 = 0
    
    # Calcular o segundo dígito verificador
    soma2 = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma2 * 10) % 11
    if digito2 == 10:
        digito2 = 0
    
    # Verificar se os dígitos calculados correspondem aos informados
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    return False

# Solicitar CPF ao usuário
cpf_usuario = input("Digite o CPF para verificar (com ou sem pontuação): ")

# Verificar e exibir o resultado
if validar_cpf(cpf_usuario):
    print("CPF válido!")
else:
    print("CPF inválido!")