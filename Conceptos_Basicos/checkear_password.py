def chequear_password():
    'Programa que le pide a un usuario una password. Si se acaban los intentos termina la ejecucion.'
    password = 'algoritmos'
    intentos = 5
    while intentos > 0:
        intento = input('Ingrese la contraseña: ')
        if intento == password:
            print('La password es correcta.' )
            break
        intentos -= 1

    if intentos == 0:
        print('Se acabaron los intentos.')

chequear_password()

    
    