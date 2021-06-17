paises = [
    { 
        'nombre': 'Chile',
        'ciudades': [{'nombre' : 'Temuco','poblacion':10 }, 
                     {'nombre' : 'Santiago', 'poblacion':20},
                     {'nombre' : 'Conce', 'poblacion':30}]
    },
    { 
        'nombre': 'Argentina',
        'ciudades': [{'nombre' : 'Buenos Aires','poblacion':40 },
         {'nombre' : 'San Martin','poblacion':50 }, 
         {'nombre' : 'Mendoza','poblacion':60 }]
    },
]

paises.append({ 
        'nombre': 'Peru',
        'ciudades': [{'nombre' : 'Cuzco','poblacion':70 },
                    {'nombre' : 'Arequipa','poblacion':80 }, 
                    {'nombre' : 'Tacna','poblacion':90 }, 
                    {'nombre' : 'Lima','poblacion':100 }]
    })

print(paises)

for pais in paises:
    for ciudad in pais['ciudades']:

        if ciudad['nombre'] == 'Temuco' and pais['nombre'] == 'Chile':
            ciudad['poblacion'] = 110 

        if ciudad['poblacion']>50:
            print( pais['nombre'] ,ciudad['nombre'])

print(paises)

for pais in paises:
    print(f" first_name El pais {pais['nombre']}")