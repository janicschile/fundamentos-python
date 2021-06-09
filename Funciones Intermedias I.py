# Ejercicio #1 + BONUS
####    
import random
def randInt(min=0, max=100):
    if (min < 0) or (max > 500) or (min > max):
        return "error de datos, reintente..."
    else:
        num = random.random() * max + min
        return round(num)
#print(randInt()) 		    # debería imprimir un número aleatorio entre 0 a 100
#print(randInt(max=50)) 	    # debería imprimir un número aleatorio entre 0 a 50
print(randInt(min=50)) 	    # debería imprimir un número aleatorio entre 50 a 100
#print(randInt(min=50, max=500))    # debería imprimir un número aleatorio entre 50 y 500
####


# BONUS II - Jugando al Loto
####    
import random

def randInt(min=0, max = 0):
    num = random.random() * max + min
    return round(num)

numerosDeLoto = 6       # cantidad de numeros de loteria
maxNumerosLoto = 41     # rango maximo de numeros del juego
minNumerosLoto = 1      # minimo valor numerico del rango de juego
numerosLoto = []        # array a almacenar resultados de numeros aleatrios del Loto
for i in range(1,100):  #  rango tiene maximo de 100, pero jamas llegara a esos bucles, esta limitado a 6 datos y BRAKE.
    if (len(numerosLoto) < numerosDeLoto):  # IF valido si array "numerosLoto" contiene x cant. de "numerosDeLoto" y BREAK
        randomNumber = randInt(min=minNumerosLoto,max=maxNumerosLoto) #Llamamos a la funcion RandInt con min=minNumerosLoto y max=maxNumerosLoto en este caso de entre 1 y 41
        # print(randomNumber)
        if randomNumber not in numerosLoto:  # Aqui garantizamos el el numero random de la fn, no exista.
            numerosLoto.append(randomNumber) # se agrega al array de seleccion
            #print(numerosLoto)
    else:
        break
print(f"Los numeros de LOTO seleccionadoa aleatoriamente son: {numerosLoto}")
####
####