#El metodo reduce esta en el modulo functools
from functools import reduce

vector = list(range(100))

vec_filter = filter(lambda v: v%15==0, vector)

vec_map = map(lambda v: v/5, vec_filter)
vec_map = list(vec_map) #convierte el resultado del map a una lista

#Ordena los pares hacia la izquierda y los impares hacia la derecha
#Descubierto por error 😅
vec_sorted = sorted(vec_map, key=lambda v: v%2, reverse=False)

vec_reversed = reversed(vec_map)

#Devuelve true si todos los elementos de una lista es True
vec_all = all(v>=0 for v in vec_map)

#Devuelve true si al menos un elemento de la lista es True
vec_any = any(v%9==0 for v in vec_map)

vec_reduce = reduce(lambda a,b:a+b, vec_map)

#Al haber sido usado por map devolvera una lista vacia
print("filter:",list(vec_filter), "Al haber sido usado por map devolvera una lista vacia")

print("map:",vec_map)

print("reversed:",list(vec_reversed))
print("sorted:",vec_sorted)

print("all:", vec_all, [v>=0 for v in vec_map])
print("any:", vec_any, [v%9==0 for v in vec_map])

print("reduce:",vec_reduce)