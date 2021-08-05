def total_productos(ruta, lista):
    #Recibe una lista de pedidos y escribe en un archivo
    #los nombres de los productos y sus cantidades totales.
    auxiliar = {}
    for pedido in lista:
        for producto in pedido:
            if producto not in auxiliar:
                auxiliar[producto] = pedido[producto]
            else:
                auxiliar[producto] += pedido[producto]
    
    with open(ruta, 'w') as destino:
        for producto in auxiliar:
            destino.write(f'{producto};{auxiliar[producto]}\n')
    return

