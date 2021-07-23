def maximo_minimo_cuadratica(a, b, c):
    'Encuentra el maximo o  el minimo de un polinomio de segundo  grado dados sus coeficientes'
    'Devuelve True si es maximo, False si es minimo'
    if not a == 0:
        xvertice =  (- b) / (2 * a)
        yvertice = (4 * a * c - b ** 2) / (4 * a)
        return (xvertice, yvertice) , a > 0
    
def raices_cuadratica(a, b, c):
    'Recibe los  coeficientes de un polinomio de segundo grado y devulve sus raices'
    'En caso de tener termino cuadratico negativo devuelve None'
    terminocuadratico = b ** 2 - 4 * a * c
    if terminocuadratico >= 0:
        primeraraiz = ((- b) + (terminocuadratico) ** 0.5) / (2 * a)
        segundaraiz = ((- b) - (terminocuadratico) ** 0.5) / (2 * a)
        return primeraraiz, segundaraiz
    return None, None

