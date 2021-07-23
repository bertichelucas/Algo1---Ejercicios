'''
Dada la cantidad de ejercicios de un examen, y el porcentaje necesario de ejercicios bien resueltos necesario para aprobar dicho examen, 
revisa un grupo de examenes. En cada paso pregunta la cantidad de ejercicios resueltos por el alumno, 
indicando con un valor centinela que no hay más examenes a revisar.
Imprime el porcentaje correspondiente a la cantidad de ejercicios resueltos respecto a la
cantidad de ejercicios del examen y una leyenda que indique si aprobó o no.
'''

def revisar_grupo_examenes(ex, perc):
    while True:
        examen = (int(input('Ingrese cant de ej resueltos, si no hay mas examenes ingrese -1 ')))
        if examen == -1:
            break
        if examen <= ex:
            resultado = (examen * 100) / ex
            print ('usted hizo el ', resultado, ' porciento de los ejercicios')
            if resultado >= perc:
                print ('usted aprobo el examen')
            else:
                print ('usted reprobo el examen')
        
revisar_grupo_examenes(10, 70)