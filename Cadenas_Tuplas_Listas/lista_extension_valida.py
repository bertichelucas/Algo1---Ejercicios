def extension_valida(ruta, formatos_admitidos):
    #Recibe una ruta y determina si su extencion es valida.
    lista = ruta.split('.')
    if lista[-1] in formatos_admitidos:
        return True
    return False

