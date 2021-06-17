# Ejercicio #1 - Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
####
x = [ [5,2,3], [10,8,9] ] 
print(f"x Antes   :{x}")
(x[1])[0] = 15
print(f"x despues :{x}")
####
####

# Ejercicio #1.1 "BONUS" - Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
####                    Pero recorrido con ciclo for.
####
def bonus(x):
    for i in range(0, len(x)):
        for j in range(0, len(x[i])):
            valor = x[i][j]
            if valor == 10:
                x[i][j] = 15
    return x
x = [ [5,2,3], [10,8,9,10] ]
print(bonus(x))
####
####


# Ejercicio #1.2 - Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
####
def listaEstudiantes(estudiantes):
    for estudiante in estudiantes:
        if estudiante['last_name'] == "Jordan":
            estudiante['last_name'] = "Bryant"
    return estudiantes

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(f"Lista Original: {students}")
print(f"Lista NUeva   : {listaEstudiantes(students)}")
####
####



# Ejercicio #1.3 - En el directorio sports_directory, cambia 'Messi' a 'Andres'

def jugadores(sports_directory):
    for deportes in sports_directory:
        for deportistas in range(len(sports_directory[deportes])):
            if sports_directory[deportes][deportistas] == "Messi" :
                sports_directory[deportes][deportistas] = "Andres"
    return sports_directory

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(jugadores(sports_directory))
####
####


# Ejercicio #1.4 - Camba el valor 20 en z a 30
####
def laZ(z):
    for i in z:
        for x in i:
            if i[x] == 20:
                i[x] = 30
    return z

z = [ {'x': 10, 'y': 20} ]
print(laZ(z))
####
####


# Ejercicio #2 - Itera a través de una lista de diccionarios : Crea una función iterateDictionary(some_list) que, 
####             dada una lista de diccionarios, la función recorra cada diccionario de la lista e imprime cada clave 
####             y el valor asociado. Por ejemplo, dada la siguiente lista:
def iterateDictionary(students):
    for listaAlumnos in range(len(students)):
        nombre = students[listaAlumnos]["first_name"]
        apellido = students[listaAlumnos]["last_name"]
        if listaAlumnos == 0:
            print("\nLISTA DE ESTUDIANTES ESTRELLAS EN DEPORTES\n==========================================\n")
        aDevolver = print(f"{listaAlumnos+1}.- {nombre} {apellido}")
    return aDevolver

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
####
####



# Ejercicio #3 - Obtén valores de una lista de diccionarios : Crea una función iterateDictionary2(key_name, some_list)
####             que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa 
####             clave para cada diccionario. Por ejemplo, iterateDictionary2 ('first_name', students) debería generar:
def iterateDictionary(key_name, students):
    for listaAlumnos in range(len(students)):
        lista = students[listaAlumnos][key_name]
        if listaAlumnos == 0 and key_name == "first_name":
            print("\nLISTA DE NOMBRES DE ESTUDIANTES ESTRELLAS EN DEPORTES\n=====================================================\n")
        if listaAlumnos == 0 and key_name == "last_name":
            print("\nLISTA DE APELLIDOS DE ESTUDIANTES ESTRELLAS EN DEPORTES\n=======================================================\n")
        aDevolver = print(f"{listaAlumnos+1}.- {lista}")
    return aDevolver

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary("first_name", students)
iterateDictionary("last_name", students)
####
####


# Ejercicio #4 - Itera a través de un diccionario con valores de listas : Crea una función printInfo(some_dict)
####             que, dado un diccionario cuyos valores son todas listas, imprima el nombre de cada clave junto con 
####             el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave.
def printInfo(dojo):
    for lugares in dojo:
        print(f"{len(dojo[lugares])} {lugares.upper()}")
        for ciudades in range(len(dojo[lugares])):
            #print(f"ciudad: {ciudades} largo: {len(dojo[lugares])-1}")
            print(dojo[lugares][ciudades])
            if ciudades == len(dojo[lugares])-1:
                print("")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
####
####



