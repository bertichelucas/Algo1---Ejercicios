def producto_digital(numero):
    #Producto de todos los digitos de un numero.
    lista_num = []
    for num in str(numero):
        lista_num.append(int(num))
    return funcion_recursiva(lista_num)
    

def funcion_recursiva(lista_num):
    if len(lista_num) == 1:
        return lista_num[0]
    else:
        numero = lista_num[1]
        lista_num.pop(1)
        return numero * funcion_recursiva(lista_num)

