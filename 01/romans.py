def int_to_roman(num):
    numeros = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    roman = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    resultado = ''
    i = 0
    while num > 0:
        for _ in range(num // numeros[i]):
            resultado += roman[i]
            num -= numeros[i]
        i += 1
    return resultado



def roman_to_int(s):
    numeros = {
        "M": 1000, "CM": 900, "D": 500, "CD": 400,
        "C": 100, "XC": 90, "L": 50, "XL": 40,
        "X": 10, "IX": 9, "V": 5, "IV": 4,
        "I": 1
    }
    
    i = 0
    total = 0
    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in numeros:
            total += numeros[s[i:i+2]]
            i += 2
        else:
            total += numeros[s[i]]
            i += 1
    return total
