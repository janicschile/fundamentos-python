def primos(maximo):

    array = []                              # Se declara array inicial vacia.
    for x in range(2, maximo + 1 , 1):      
        array.append(x)                     # Agregamos los datos a la variable array desde 2 hasta el maximo.

    for i in range(2, maximo + 1, 1):
        for x in range(2, maximo + 1, 1):
            if (x * i) <= maximo:           # Garantizamos que solo llegue hasta el maximo dado en la funcion
                if (x * i) in array:        # Si el valor de x*i se encuentra en el array, seguimos
                    array.remove(x * i)     #  Eliminamos el valor del array
    return array

maximo= 100
print(primos(maximo))

# Ref: https://www.superprof.es/apuntes/escolar/matematicas/aritmetica/divisibilidad/numeros-primos.html
# Web que me ilumino con la Criba de Eratóstenes.