def main():
    print("Hola, mundo!, por que esto siempre tiene que ser el primer ejercicio")

    #mas complejo que lo que explico el profe, pero basicamente lo mismo
    #el tipo de las variables no afecta la ejecucion
    inp:int = 0
    s_repeat:str = "str_"

    while True:
        try:
            inp = int(input("Ingrese un numero: "))
            break
        except ValueError:
            print("Error, el dato ingresado no es un numero valido")


    inp_abs = abs(inp)

    print(f"El numero ingresado es {inp}")
    print(f"El doble del numero ingresado es {inp * 2}")
    print(f"Este Str se repite {inp_abs} veces: {s_repeat * inp_abs}")

    if inp > 0:
        print("El numero es positivo")
    elif inp == 0:
        print("El numero es neutro")
    else:
        print("El numero es negativo")

    #vectores
    vector = [f"vec_{v}" for v in range(3)]
    print("Vector: ", ", ".join(vector))
    print(f"Vector multiplicado por {inp_abs}: ", ", ".join(vector*inp_abs))

    vector2 = [1,2,3]
    print("Vector", vector2, "Invertido", vector2[::-1])

if __name__ == "__main__":
    main()