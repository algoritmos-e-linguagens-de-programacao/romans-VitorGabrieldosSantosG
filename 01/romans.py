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
    # Implemente sua função aqui
    pass
