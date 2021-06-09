# Ejercicio #1 - Tamaño grande: dada una lista, escriba una función que cambie todos los números positivos de la lista a "big".
####                            Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores son ahora
####                            [-1, "big", "big", -5]
array = [-1,3,5,-5]
def big(array):
    for i in range(1, len(array)):
        if (array[i] > 0 ):
            array[i] = "big"    
        
        #console.log(array[i])
    return array
print("Nuevo array al reemplazar positivos por big: " , big(array))
####
####



# Ejercicio #2 - Contar positivos : dada una lista de números, cree una función para reemplazar el último valor 
####                                con el número de valores positivos. 
####                                (Tenga en cuenta que cero no se considera un número positivo).
####                   Ejemplo: count_positives([- 1, 1, 1, 1 ]) cambia la lista original a [-1, 1, 1, 3] y la devuelve
####                   Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista a [1, 6, -4, -2, -7, 2] y la devuelve
def laSuma(arrayPositivos):
    suma = 0
    for i in range(0,len(arrayPositivos)):
        if (arrayPositivos[i] > 0):
            suma = (suma + 1)
    arrayPositivos[len(arrayPositivos)-1] = suma
    return arrayPositivos

arrayPositivos = [-1,1,1,1]
#arrayPositivos = [1, 6, -4, -2, -7, -2]
print(laSuma(arrayPositivos))
####
####



# Ejercicio #3 - Suma total : crea una función que toma una lista y devuelve la suma de todos los valores de la matriz.
####                          Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
####                          Ejemplo: sum_total ([6,3, -2]) debería devolver 7
####
def sumaArray(array):
    suma = 0
    for i in range(0,len(array)):
        suma = suma + array[i]
        #console.log(array[i])
    return suma
#array = [1,2,3,4]
array = [6,3, -2]
print(" La suma de array es: " , sumaArray(array));
####
####


# Ejercicio #4 - Promedio : crea una función que toma una lista y devuelve el promedio de todos los valores.
####                        Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
####
def promedioArray(array):
    suma = 0
    for i in range(0,len(array)):
        suma = suma + array[i]
        #console.log(array[i])
    resultado = suma/len(array)
    return resultado
array = [1,2,3,4]
print(" El promdio del array es: " , promedioArray(array));
####
####


# Ejercicio #5 - Longitud : crea una función que toma una lista y devuelve la longitud de la lista.
####                        Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
####                        Ejemplo: longitud ([]) debería devolver 0
####
def longitudArray(array):
    if len(array) > 0:
        return len(array)
    else:
        return 0
array = [1,2,3,4]
#array = []
print(" Longitud del array es: " , longitudArray(array));
####
####


# Ejercicio #6 - Mínimo : crea una función que tome una lista de números y devuelva el valor mínimo en la lista. 
####                      Si la lista está vacía, haga que la función devuelva False.
####                      Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
####                      Ejemplo: mínimo ([]) debería devolver False
def menorElem(array):
    if len(array) > 0:
        menorHastaAhora = array[0]
        for i in range(0,len(array)):
            posicionArr = 0
            if ( menorHastaAhora >= array[i]):
                posicionArr = i
                menorHastaAhora = array[i]           
            else:
                menorHastaAhora = array[posicionArr]
    else:
        return False
    return menorHastaAhora;

array = [-3,3,5,7]
#array = []
print("El numero menor es:" , menorElem(array) );
####
####



# Ejercicio #7 - Máximo : crea una función que toma una lista y devuelve el valor máximo en la matriz. 
####                      Si la lista está vacía, haga que la función devuelva False.
####                      Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
####                      Ejemplo: máximo ([]) debería devolver False
####
def mayorElem(array):
    if len(array) > 0:
        mayorHastaAhora = array[0]
        for i in range(0,len(array)):
            posicionArr = 0
            if ( mayorHastaAhora <= array[i]):
                posicionArr = i
                mayorHastaAhora = array[i]           
            else:
                mayorHastaAhora = array[posicionArr]
    else:
        return False
    return mayorHastaAhora;

array = [37,2,1, -9]
#array = []
print("El numero mayor es:" , mayorElem(array) );
####
####


# Ejercicio #6 - Análisis final : crea una función que tome una lista y devuelva un diccionario que tenga la suma total, 
####                              promedio, mínimo, máximo y longitud de la lista.
####                              Ejemplo: ultimate_analysis ([37,2,1, -9]) 
####                              debería devolver {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}
def seFueronAlChanchoXD(array):
    ################################################
    # CALCULO DE SUMA
    #
    suma = 0
    for i in range(0,len(array)):
        suma = suma + array[i]
    ################################################
    #print(suma)
    ################################################


    ################################################
    #CALCULO PROMEDIO
    #
    promedio = 0
    for i in range(0,len(array)):
        promedio = promedio + array[i]
        #console.log(array[i])
    promedio = promedio/len(array)
    ################################################
    #print(promedio)
    ################################################
    

    ################################################
    # VALOR MINIMO
    #
    menorHastaAhora = array[0]
    for i in range(0,len(array)):
        posicionArr = 0
        if ( menorHastaAhora >= array[i]):
            posicionArr = i
            menorHastaAhora = array[i]           
        else:
            menorHastaAhora = array[posicionArr]
    ################################################
    #print(menorHastaAhora)
    ################################################


    ################################################
    #### VALOR MAXIMO
    #
    mayorHastaAhora = array[0]
    for i in range(0,len(array)):
        posicionArr = 0
        if ( mayorHastaAhora <= array[i]):
            posicionArr = i
            mayorHastaAhora = array[i]           
        else:
            mayorHastaAhora = array[posicionArr]
    ################################################
    #print(mayorHastaAhora)
    ################################################

    ################################################
    #### VALOR LONGITUD
    #
    ################################################
    #print(len(array))
    ################################################
    return [{'total': suma, 'promedio': promedio, 'minimo': menorHastaAhora, 'maximo': mayorHastaAhora, 'longitud': len(array)}]
    
array = [37,2,1, -9]
#array = []
print("El retorno de datos es:\n" , seFueronAlChanchoXD(array) );




# Ejercicio #7 - Lista inversa : crea una función que tome una lista y la devuelva con los valores invertidos. 
####                             Haz esto sin crear una segunda lista. 
####                             (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
####                             Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def listaInversa(lista=[]):
    if len(lista) == 0:
        return lista
    else:

        return lista[::-1]

lista = [37,2,1, -9]
print (listaInversa(lista))


