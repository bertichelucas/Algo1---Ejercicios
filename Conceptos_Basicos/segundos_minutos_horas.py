def segundos(h, m, s):
    'Recibe una cantidad de horas, minutos y  segundos y devuelve la cantidad total de segundos'
    stotales = 3600 * h + 60 * m + s
    return stotales



def inversasegundos(s):
    'Recibe una cantidad de segundos y  devuelve el equivalente en horas minutos y segundos '
    h = s // 3600
    m = (s % 3600) // 60
    s = s % 60
    return h, m ,s 

