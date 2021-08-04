def elementos_menor_mayor(tupla):
    #Recibe una tupla y indica si
    #los elementos estan ordenandos de menor a mayor.
    c = tupla [0]
    for elemento in tupla:
        if elemento >= c:
            c = elemento
        else:
            return False
    return True


