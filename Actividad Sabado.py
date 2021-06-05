# Ejercicio #1 - Imprime todos los números del 0 al 10
for x in range(10 + 1):
    print(x)
####
####


# Ejercicio #2 - Imprime todos los números impares del 0 al 3000
for x in range(1, 10 + 1, 2):
    print(x)
####
####


# Ejercicio #3 - Crear una función que recorra cada valor de la lista e imprima cada valor
def recorrerLista(lista):
    for valor in lista:
        print(valor)
recorrerLista(["Santiago","Concepcion","Temuco","Iquique","Antofagasta"])
####
####       
    

# Ejercicio #4 - Crea una función que toma una lista como argumento y devuelve una suma de todos sus valores
def recorrer_suma(lista):
    suma = 0
    for valor in lista:
        suma += valor
    return suma
print(recorrer_suma([1,2,3,4,5,6]))
    



#EJERCICIO GRUPO 1: Crea una función que tome una lista y devuelva el primer y el último valor de la lista. 
#                   Si la longitud de la lista es menor que 2, haga que devuelva False.
def buscaLista(lista):
    if len(lista) < 2:
        return False
    else:
        primero = lista[0]
        ultimo = lista[len(lista) -1]
    return primero, ultimo
    
print(buscaLista([1,2,3]))


# Ejercicio Grupal
def ejercicio(lista=[]):
    if len(lista) < 2:
        return False, False
    else:
        primer = lista[0]
        ultimo = lista[-1]
        #ultimo = lista[len(lista)+1]
        return primer, ultimo
    
lista_prueba1 = [1, 2, 3, 4]
lista_prueba2 = [2]
print(lista_prueba1[0])
primer, ultimo = ejercicio(lista_prueba1)
print(f"el primero es {primer} y el ultimo es {ultimo}")




igual, aux = 0, 0
texto = "hannah"
for ind in reversed(range(0, len(texto))):
    if texto[ind].lower() == texto[aux].lower():
        igual += 1
        aux += 1
if len(texto) == igual:
    print("El texto es palindromo!")
else:
    print("El texto no es palindromo!")

