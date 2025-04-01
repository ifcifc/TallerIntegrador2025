import random
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lista.append(10)
lista[9] = 99

print("Lista", lista)
print("Lista",lista[0:5])

tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Tupla", tupla)
try:
    print("Tuplas estaticas, tirara un error al ejecutar")
    tupla[8] = 99  # pylint: disable=unsupported-assignment-operation
except TypeError as e:
    print("Error", e)

#Esto solo funciona con tuplas, las listas tirara un error
TEXTO = "Esto es una prueba %d y de %s" % (10, "tuplas")# pylint: disable=C0209
print("Texto", TEXTO)

# Esto es una tupla de schrodinger, es una tupla y una lista a la vez, hasta que se ejecuta
if random.randint(0, 1) == 0:
    tupla = list(tupla)

print("Esto puede o no fallar, cosas raras de python")
tupla[8] = 99
print("Tupla", tupla)