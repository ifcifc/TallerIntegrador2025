print("Los range son generadores")
rng = range(999999999)
print("Termino el range")
print("Las listas no son generadores")
list(range(49999999))
print("Termino la lista")

try:
    #Los range no son iterator
    print(next(rng))
except Exception as e:
    print(e)