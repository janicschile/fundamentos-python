# Para crear un módulo Python personalizado, ¡simplemente definirás varias funciones o métodos en una sola clase! Hablaremos sobre 
# las clases pronto, por ahora puedes usar el código a continuación y seguir el patrón para llamar a los métodos como se muestra a 
# continuación.
# Crearás los siguientes métodos de la biblioteca Underscore como métodos del objeto "_". Presta atención a lo que tienes que cambiar,
# en términos de parámetros para cada método, así como la implementación.
# En cada uno de los siguientes métodos, el primer parámetro, self , se pasa implícitamente (nuevamente, más sobre esto en el próximo 
# capítulo). Los únicos parámetros de los que debes preocuparte por ahora son iterables y devolución de llamada . Iterable será la 
# lista que se pasa y la devolución de llamada será la función lambda.

class Underscore:
    def map(self, iterable, callback):
        dobles = []
        for i in iterable:
            dobles.append(callback(i))
        return dobles
        
    def find(self, iterable, callback):
        for i in iterable:
            if callback(i):
                return i

    def filter(self, iterable, callback):
        pares = []
        for i in iterable:
            if callback(i):
                pares.append(i)
        return pares

    def reject(self, iterable, callback):
        impares = []
        for i in iterable:
            if callback(i):
                impares.append(i)
        return impares

# has creado una libreria con 4 métodos, se crea la instancia de la clase

_ = Underscore() # sí, estamos configurando una instancia a una variable que es un guión bajo
# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# print(evens) debe retornar [2, 4, 6] después que termines de implementar el código de arriba

print("Map:", _.map([1,2,3], lambda x: x*2)) # debe retornar [2,4,6]
print("Find > 4:", _.find([1,2,3,4,5,6], lambda x: x>4)) # debe retornar el primer valor que es mayor que 4
print("Filter Pares:", _.filter([1,2,3,4,5,6], lambda x: x%2==0)) # debe retornar [2,4,6]
print("Reject Pares:", _.reject([1,2,3,4,5,6], lambda x: x%2!=0)) # debe retornar [1,3,5]
