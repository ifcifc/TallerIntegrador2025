def decorador1(func):
    #Devuelve otra funcion que ara algo antes y despues de la funcion decorada
    #wrapper recibe los argumentos que seran pasados a la funcion decorada
    def wrapper(value):
        print("Ejecutando decorador1")
        ret = func(value)
        print("Fin de decorador1")
        return ret
    return wrapper

@decorador1
def funcion_decorada(value):
    print("Ejecutando funcion_decorada")
    return value ** 2

print(funcion_decorada(5)) #25
