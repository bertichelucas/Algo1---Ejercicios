def agenda():
    #Agenda Telefonica, pregunta al usuario por un nombre
    #Si no esta en la agenda, lo agrega y pide su numero
    #Si esta en la agenda, da la opcion de cambiar de numero.
    dic = {}
    nombre = ''
    while True:
        nombre = input('ingrese un nombre: ')
        if nombre == '*':
            break
        if nombre not in dic:
            telefono = (input('ingrese el numero de telefono: '))
            dic[nombre] = telefono
        else:
            print('el telefono es', dic[nombre])
            nuevotel = input('si el num es incorrecto ingreselo nuevamente, de lo contrario ingrese "no" ')
            if nuevotel != 'no':
                dic[nombre] = nuevotel



        