def argumentos_posicionales(*args):
    for i, v in enumerate(args):
        print(f"arg[{i}] = {v}")

def argumentos_clave_valor(**kwargs):
    for clave, valor in kwargs.items():
        print(f"key[{clave}]: {valor}")


def operacion(a,b,c): 
    return (a+c)*b
    

argumentos_posicionales(1,2,3,4,5,6)
argumentos_clave_valor(a=3, b="hola", c=False, noce=argumentos_posicionales)

args = [2, 4, 6]
kwargs = {
    "c": 6,
    "a": 2,
    "b": 4 
}


print("Argumento posicionales en un metodo:", operacion(*args))
print("Argumentos con nombre en un metodo:", operacion(**kwargs))