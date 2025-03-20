# Índice
- [Multiplicar String](#multiplicar-string)
- [Multiplicar Vector](#multiplicar-vector)
- [Indicar tipo de variable](#indicar-tipo-de-variable)
- [Generar errores](#generar-errores)
- [Slice Vector](#slice-vector)
- [Inverir Vector](#inverir-vector)
- [Funciones anónimas](#funciones-anónimas)
- [Argumentos Posicionales (*args)](#argumentos-posicionales-args)
- [Argumentos con Nombre o Clave-Valor (**kwargs)](#argumentos-con-nombre-o-clave-valor-kwargs)
- [Pasar Argumentos Posicionales/Clave-Valor a un metodo](#pasar-argumentos-posicionalesclave-valor-a-un-metodo)
- [Equivalentes a Stream de java](#equivalentes-a-stream-de-java)

# Multiplicar String
```py
    hola = "Hola"
    print(hola * 3)
```
### Salida
```py
    "HolaHolaHola"
```

# Multiplicar Vector
```py
    hola = ["Hola"]
    print(hola * 3)
```
### Salida
```py
    ["Hola", "Hola", "Hola"]
```

# Indicar tipo de variable
- Solo un indicador no afecta en la ejecucion

```py
    VARIABLE:TIPO
    hola:str = "Hola"
```

# Generar errores
```py
    raise Exception(MSG)
```

# Slice Vector
- Slice 3 argumentos [desde:hasta:salto], por defecto salto tiene el valor 1
```py
    Vector original: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Vector [:5:1] o [:5]: [0, 1, 2, 3, 4]
    Vector [:5:2]: [0, 2, 4]
    Vector [:5:2]: [0, 3]
```
### Ejemplo
```py
    vec = list(range(10))
    print(vec[:5])
```

# Inverir Vector
```py
    hola = [1,2,3]
    print(hola[::-1])
```
### Salida
```py
    [3, 2, 1]
```

# Funciones anónimas
- Funciones de una sola linea
```py
    lambda argumentos : logica
```
- En estas funciones no se pueden realizar asignacion en una variable
```py
    #No funciona
    isOn = False
    toggle =  lambda : isOn = not IsOn
```

### Ejemplo
```py
    sumar = lambda a, b=0: a + b

    print(sumar(2,2))
    print(sumar(2))
```

# Argumentos Posicionales (*args)
- Permine pasar a una funcion un numero indeterminado de argumentos en una tupla
```py
    def argumentos_posicionales(*args):
        for i, v in enumerate(args):
            print(f"arg[{i}] = {v}")
    argumentos_posicionales(1,2,3)
```

### Salida
```py
    arg[0] = 1
    arg[1] = 2
    arg[2] = 3
```

# Argumentos con Nombre o Clave-Valor (**kwargs)
- Permite pasar un diccionario como argumentos de una funcion
```py
    def argumentos_clave_valor(**kwargs):
        for clave, valor in kwargs.items():
            print(f"key[{clave}]: {valor}")
    argumentos_clave_valor(a=3, b="hola", c=False)
```

### Salida
```py
    key[a]: 3
    key[b]: hola
    key[c]: False
```

# Pasar Argumentos Posicionales/Clave-Valor a un metodo
```py
    def operacion(a,b,c): 
        return (a+c)*b
        
    args = [2, 4, 6]
    kwargs = {
        "c": 6,
        "a": 2,
        "b": 4 
    }

    print("Args:", operacion(*args))
    print("Kwargs:", operacion(**kwargs))
```

### Salida
```py
    Args: 32
    Kwargs: 32
```

# Equivalentes a Stream de java
| Método   | Argumentos                          | Descripción breve                                   |
|----------|-------------------------------------|---------------------------------------------------|
| filter   | function, iterable                 | Filtra elementos de un iterable según una función |
| map      | function, iterable                 | Aplica una función a cada elemento de un iterable |
| sorted   | iterable, key (opcional), reverse (opcional) | Ordena elementos de un iterable                  |
| reversed | iterable                           | Devuelve un iterable invertido                    |
| all      | iterable                           | Verifica si todos los elementos son True          |
| any      | iterable                           | Verifica si algún elemento es True                |
| reduce   | function, iterable, initializer (opcional) | Reduce un iterable a un solo valor usando una función |

__Los metodos filter, map y reversed devuelven iterables, si el resultado de una de estas operaciones es utilizado por otra, y si se intenta utilizar de nuevo el resultado devolvera una lista vacia (se consume)__

### Ejemplo
```py
    vector = list(range(100))
    vec_filter = filter(lambda v: v%15==0, vector)
    vec_map = map(lambda v: v/5, vec_filter)
    print("filter:",list(vec_filter))
    print("map:",list(vec_map))
```

### Salida
```py
    filter: [] #Al haber sido usado(consumido) por el map devolvera una lista vacia
    map: [0.0, 3.0, 6.0, 9.0, 12.0, 15.0, 18.0]
```
