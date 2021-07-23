def entero_a_romano(num):
    'Dado un numero entero lo transforma a romano. El numero debe estar entre 1 y 3999'
    valores = [1000, 900, 500, 400, 100, 90, 50 ,40, 10, 9, 5, 4, 1]
    romanos = ['M','CM','D','CD','C', 'XC', 'L', 'XL','X', 'IX', 'V', 'IV', 'I']

    resultado = ''
    i = 0
    while num > 0:
        for _ in range(num // valores[i]):
            resultado += romanos[i]
            num -= valores[i]
        i += 1
    
    return resultado
    