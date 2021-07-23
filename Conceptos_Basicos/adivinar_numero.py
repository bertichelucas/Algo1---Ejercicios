from random import randrange

def adivinarnumero():
    'Programa que genera un numero aleatorio entre el 1 y 1000 y permite al usuario ingresar numeros hasta adivinarlo.'
    adivina = randrange(1,1000)
    value = 0
    while value != adivina:
        value = int(input('ingrese un numero '))
        if value < adivina:
            print(value, 'es menor, intente de nuevo')
        elif value > adivina:
            print(value, 'es mayor, intente de nuevo')
        else:
            print('el numero ingresado es correcto')
            break

adivinarnumero()