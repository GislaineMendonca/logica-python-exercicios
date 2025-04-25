# Crie uma função que converte números inteiros em algarismos romanos e vice-versa.

class RomanConverter:
    def __init__(self):
        # Mapeamento de valores inteiros para algarismos romanos
        self.int_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        # Mapeamento de algarismos romanos para valores inteiros
        self.roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
    
    def to_roman(self, num):
        """Converte um número inteiro para algarismo romano"""
        if not isinstance(num, int) or num <= 0 or num > 3999:
            raise ValueError("O número deve ser um inteiro entre 1 e 3999")
        
        roman_num = []
        for value, symbol in self.int_to_roman:
            while num >= value:
                roman_num.append(symbol)
                num -= value
        return ''.join(roman_num)
    
    def to_int(self, roman):
        """Converte um algarismo romano para número inteiro"""
        if not isinstance(roman, str) or not roman:
            raise ValueError("A entrada deve ser uma string não vazia")
        
        roman = roman.upper()
        total = 0
        prev_value = 0
        
        for char in reversed(roman):
            if char not in self.roman_to_int:
                raise ValueError(f"Caractere inválido em numeral romano: {char}")
            
            value = self.roman_to_int[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        
        # Verifica se a conversão reversa produz o mesmo numeral romano
        if self.to_roman(total) != roman:
            raise ValueError(f"{roman} não é um numeral romano válido")
        
        return total

# Função de conveniência para usar o conversor
def convert_number(value):
    converter = RomanConverter()
    try:
        if isinstance(value, int):
            return converter.to_roman(value)
        elif isinstance(value, str):
            return converter.to_int(value)
        else:
            raise ValueError("Tipo de entrada inválido. Use int ou str.")
    except ValueError as e:
        return f"Erro: {str(e)}"

# Exemplos de uso
if __name__ == "__main__":
    print("2024 em romanos:", convert_number(2024))  # MMXXIV
    print("MMXXIV em inteiro:", convert_number("MMXXIV"))  # 2024
    
    print("3999 em romanos:", convert_number(3999))  # MMMCMXCIX
    print("MMMCMXCIX em inteiro:", convert_number("MMMCMXCIX"))  # 3999
    
    # Testando erros
    print(convert_number(0))        # Erro: número fora do intervalo
    print(convert_number(4000))     # Erro: número fora do intervalo
    print(convert_number("IIII"))   # Erro: numeral romano inválido
    print(convert_number(3.14))     # Erro: tipo inválido