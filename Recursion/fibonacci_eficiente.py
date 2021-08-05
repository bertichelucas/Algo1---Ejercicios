
def fibonacci(n):
    #Utiliza diccionarios para guardar los fibonaccis ya calculados
    #De esta manera no tiene que volver a calcularlos.
    dict_fibonacci = {0 : 0, 1 : 1}
    dict_fibonacci = funcion_recursiva(n, dict_fibonacci, n)
    return dict_fibonacci[n]

def funcion_recursiva(n, dict_fibonacci, constante):
    if n == 0 or n == 1:
        return dict_fibonacci
    if (n - 1) not in dict_fibonacci:
        return funcion_recursiva(n - 1, dict_fibonacci, constante)
    while n != constante + 1:
        dict_fibonacci[n] =  dict_fibonacci[n - 1] + dict_fibonacci[n - 2]
        n += 1
    return dict_fibonacci
    

