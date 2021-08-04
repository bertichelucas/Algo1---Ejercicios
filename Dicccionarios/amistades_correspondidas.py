'''
Se tiene un diccionario en el que la clave es el nombre de una persona y el valor una lista con sus amigos. 
Ejemplo: {'Juan': ['Caro', 'José', 'Daniela', 'Alejandro'], 'Caro': ['José', 'Daniela'], 'José': ['Caro', 'Juan'], 'Daniela': [], 'Alejandro': ['Caro', 'José', 'Juan']}

Se quiere obtener una lista de tuplas con aquellas amistades que son correspondidas. 
Se considera correspondida la amistad si un nombre está en mi lista y yo estoy en la lista de ese nombre. 
Según el ejemplo dado, debe devolver: [('Juan', 'José'), ('José', ‘Juan’), ('Juan', 'Alejandro'), ('Caro', 'José'), ('José', ‘Caro’) ('Alejandro', 'Juan')]
'''

def amistades_correspondidas(diccionario):
    resultado = []
    for persona in diccionario:
        for amigo in diccionario[persona]:
            if persona in diccionario[amigo]:
                resultado.append((persona, amigo))
    return resultado

ejemplo =  {
    'Juan': ['Caro', 'José', 'Daniela', 'Alejandro'], 
    'Caro': ['José', 'Daniela'], 
    'José': ['Caro', 'Juan'], 
    'Daniela': [], 
    'Alejandro': ['Caro', 'José', 'Juan']
    }
print(amistades_correspondidas(ejemplo))