# Ejercicios #1 - Cuenta regresiva : crea una función que acepte un número como entrada.
#                                    Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número 
#                                    (como el elemento 0) hasta 0 (como el último elemento).
#                                    Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
###
array = []
def regresiva(cantMax):
    for x in range(cantMax, 0-1, -1):
        #print(cantMax)
        array.append(cantMax)
        cantMax -= 1

cantMax = 50
regresiva(cantMax)
print(array)
###
###



# Ejercicios #2 - Imprimir y volver : crea una función que recibirá una lista con dos números. 
#                                     Imprima el primer valor y devuelva el segundo.
#                                     Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
###
def lista(listaArray):
    print("Impreso en Funcion: " , listaArray[0])
    return listaArray[1]
listaArray = [1,2]
print("Devuelto por return:" , lista(listaArray))
###
###


# Ejercicios #3 - First Plus Length : crea una función que acepta una lista y devuelve la suma del primer 
#                                     valor de la lista más la longitud de la lista.
###
def listaSuma(sumaArray):
    resultado = sumaArray[0] + len(sumaArray)
    return resultado
sumaArray = [1,2,3,4,5,6]
print("El valor de la suma es:" , listaSuma(sumaArray))
###
###


# Ejercicios #4 - Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista 
#                       que contenga solo los valores de la lista original que sean mayores que su segundo valor. 
#                       Imprima cuántos valores son y luego devuelva la nueva lista. 
#                       Si la lista tiene menos de 2 elementos, haga que la función devuelva False
#
#                       Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
#                       Ejemplo: values_greater_than_second ([3]) debería devolver False
###
def valores(array):
    arrayfinal = []
    if len(array) > 1:
        for i in range(0,len(array)-1):
            if array[i] > array[i+1]:
                arrayfinal.append(array[i])
    else:
        if len(array) == 0: 
            return "ADVERTENCIA: El Array debe tener datos para procesar"
        else:
            return False
    return arrayfinal

array = [5,2,3,2,1,4]
#array = [3,2]
print(valores(array))
###
###



# Ejercicios #5 - Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: 
#                                            tamaño y valor. La función debe crear y devolver una lista cuya longitud 
#                                            es igual al tamaño dado y cuyos valores son todos los valores dados.
#
#                                            Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
#                                            Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
###
array = []
def dosListas(a,b):
    for i in range(0,a):
        array.append(b)
    return array
print(dosListas(4,7))
array = []              # Vaciamos el array para la proxima consulta
print(dosListas(6,2))
###
###