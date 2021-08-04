def main():
    #Articulos y ejemplos de ciclos.
    cantidad = int(input('Cuantos articulos hay?: '))

    total = 0
    for i in range(cantidad):
        precio = float(input('ingresa un numero: '))
        total = total + precio
        print ('el total es: ', total)

main()

'''
INGRESA UN NUMERO: 8
La suma es: 8
INGRESA UN NUMERO: 3
La suma es: 11
INGRESA UN NUMERO: 1 
La suma es: 12
'''

#quiero hacer la misma funcion pero con while, en un ciclo indefinido

def main2():

    continuar = True

    total = 0
    while continuar:
        precio = float(input('ingresa un numero: '))
        total = total + precio
        print ('el total es: ', total)

        r = input('Hay mas articulos?')
        if r == "no":
            continuar = False

main2()

def main3():
    #Este tercero funciona ingresando valores hasta que metes el *
    s = input('ingresa el precio (* para terminar): ')


    total = 0
    while s!= '*':
        total = total + float(s)
        print ('el total es: ', total)

        s = input('ingresa el precio (* para terminar): ')
        
main3()

def main4():
    #Este cuarto funciona sin repetir linea y termina con el break y usa el continuar
    total = 0
    while True:
        s = input('ingresa el precio (* para terminar): ')
        if s == '':
            continue
        if s == '*':
            break
        total = total + float(s)
        print ('el total es: ', total)

main4()

