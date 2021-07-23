

def imprimir_promedio_notas():
    'Calcula e imprime un promedio de notas dadas por entrada.'
    sum, cant = 0, 0

    r = ''
    while r != 'no':
        while not r.isnumeric():
            r = input('Ingrese una nota: ')

        sum += int(r)
        cant += 1
        r = input('Desea ingresar otra nota? (si/no): ')
    
    return sum / cant

print(imprimir_promedio_notas())

