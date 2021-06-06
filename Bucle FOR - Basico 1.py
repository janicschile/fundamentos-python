# Ejercicio #1 - Básico : imprime todos los enteros del 0 al 150.
maximo = 150
for x in range(maximo + 1):
    print(x)
###
###




# Ejercicio #2 - Múltiplos de cinco : imprime todos los múltiplos de 5 de 5 a 1,000
maximo = 1000
for x in range(0, maximo + 1, 5):
    print(x)
###
###




# Ejercicio #3 - Contar, Dojo Way : imprime enteros del 1 al 100. 
#                                   Si es divisible por 5, imprima "Coding" en su lugar.  
#                                   Si es divisible por 10, imprima "Coding Dojo".
def divisible(maximo):
    for x in range(1, maximo + 1 , 1):
        if (x/10).is_integer():
            print(f"{x} Coding Dojo")
            #print("Coding Dojo")
            continue
        elif (x/5).is_integer():
            print(f"{x} Coding")
            #print("Coding")
            continue 
        else:
            print(x)
    return "" # <--- La unica forma de eliminar el "None"
cantMax = 101
print(divisible(cantMax))
###
###




# Ejercicio #4 - ¡Uf, Eso es bastante grande!: suma enteros impares de 0 a 500,000 e imprime la suma final.
def impares(maximo):
    suma = 0
    for x in range(1, maximo + 1, 2):
        suma = suma + x
        #print(f"Impar: {x} - Suma: {suma}")
        #print(suma)
    return suma
cantMax = 500000
#print("La suma total es de: " + str(impares(cantMax)))                             # VALOR BRUTO
#print("La suma total es de: " + format(impares(cantMax), ','))                     # VALOR CON COMAS
print("La suma total es de: " + "{:,}".format(impares(cantMax)).replace(",","."))   # VALOR CON PUNTOS
###
###




# Ejercicio #5 - Cuenta regresiva por cuatro : imprime números positivos del 2018 al 0, restando 4 en cada iteración.
def regresiva(cantMax):
    print(cantMax)
    cantMax -= 4
    if cantMax > 0:
        regresiva(cantMax)
    else:
        print("No es posible seguir restando")
cantMax = 2018
regresiva(cantMax)
###
###


# Ejercicio #6 - Contador flexible : establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando 
#                                    por highNum, imprima solo los enteros que son múltiplos de mult. 
#                                    Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 
#                                    (en líneas sucesivas)
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if (i/mult).is_integer():
        print(i)
###
###

