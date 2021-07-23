def es_bisiesto(ano):
    'Define si un anio es bisiesto o no'
    return ano % 4 == 0 and ((ano % 100 == 0 and ano % 400 == 0) or ano % 100 != 0)


def dias_mes(m , a):
    'Dado un dia y un mes devuelve la cantidad de dias del mes'
    if m < 8 and m % 2 != 0:
        return 31
    elif m == 2 and es_bisiesto(a) == True:  
        return 29
    elif m < 8 and m % 2 == 0:
        return 30
    elif m % 2 != 0:
        return 30
    return 31 
            
def findemes(d, m , a):
    'Dada una fecha en formato dia mes anio devuelve los dias faltantes hasta fin de mes'
    dias = dias_mes(m, a)
    return dias - d

def findeano(d, m , a):
    'Dada una fecha en formato dia mes anio devuelve los dias faltantes hasta fin de anio'
    finales  = findemes(d, m, a)
    for i in range (m, 12):
        finales += dias_mes(m, a)
    return finales

def principiodeano(d, m, a):
    'Dada una fecha en formato dia mes anio devuelve los dias transcurridos desde principios de anio'
    if es_bisiesto(a) == True:
        return 364 - findeano(d, m ,a)
    return 365 - findeano(d, m, a)
