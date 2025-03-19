def ingreso_numero(msg:str="Ingrese un numero: ")->int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Error, el dato ingresado no es un numero valido")

def suma(a:int, b:int)->int:
    return a + b

def main():
    num1 = ingreso_numero()
    num2 = ingreso_numero("Ingrese segundo numero: ")
    print(f"Suma de {num1} + {num2} =",suma(num1, num2))

    if input("Generar error? (s/n):") == "s":
        raise Exception("Error")

if __name__ == "__main__":
    main()