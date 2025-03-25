# Índice
### Conceptos Básicos  
- [Nomenclatura en Python](#nomenclatura-en-python)  
- [Indicar tipo de variable](#indicar-tipo-de-variable)  
- [Generar errores](#generar-errores)  

### Operaciones con Listas  
- [Multiplicar String](#multiplicar-string)  
- [Multiplicar Lista](#multiplicar-vector)  
- [Slice Lista](#slice-vector)  
- [Inverir Lista](#inverir-vector) 
- [Extender Lista](#extender-lista) 
- [Contar elementos de una Lista](#contar-elementos-de-una-lista)

### Funciones y Métodos  
- [Funciones lambda](#funciones-lambda)  
- [Funcion for de una linea](#funcion-for-de-una-linea)  
- [Funcion Help](#funcion-help)  

### Manejo de Argumentos en Funciones  
- [Argumentos Posicionales (*args)](#argumentos-posicionales-args)  
- [Argumentos con Nombre o Clave-Valor (**kwargs)](#argumentos-con-nombre-o-clave-valor-kwargs)  
- [Pasar Argumentos Posicionales/Clave-Valor a un metodo](#pasar-argumentos-posicionalesclave-valor-a-un-metodo)  

### Operaciones con Iterables  
- [Iterable](#iterable)  
    - [Método next](#metodo-nextiterable-obtiene-el-siguiente-elemento)
    - [Método tee](#metodo-teeiterable-copia-un-iterable)
    - [Método islice](#metodo-isliceiterable-stop-crea-de-un-iterable-hasta-una-cantidad-especificada-de-elementos)
    - [Método reduce](#metodo-reducefunc-iterable-aplica-una-funcion-a-un-iterable-reduciéndolo-a-un-único-valor)
    - [Sets](#sets)
- [Generadores](#generadores)
    - [Yield From](#yield-from)
- [Equivalentes a Stream de java](#equivalentes-a-stream-de-java)  



# Nomenclatura en Python
| Elemento          | Convención de Nomenclatura |
|--------------------|----------------------------|
| Variables          | `snake_case`              |
| Funciones          | `snake_case`              |
| Clases             | `CamelCase`               |
| Constantes         | `UPPER_SNAKE_CASE`        |
| Módulos            | `snake_case`              |
| Paquetes           | `snake_case`              |
| Métodos/Atributos Privados   | `_snake_case`             |

# Multiplicar String
```py
    hola = "Hola"
    print(hola * 3)
```
### Salida
```py
    "HolaHolaHola"
```

# Multiplicar Lista
```py
    hola = ["Hola"]
    print(hola * 3)
```
### Salida
```py
    ["Hola", "Hola", "Hola"]
```

# Extender Lista
```py
    a = [12,9,10]
    b = [4,5,6]

    a.extend(b)

    #Concatena las lista en una nueva, funciona con tuplas
    c = a + b

    print(a)
    print(c)
```
### Salida
```py
    [12, 9, 10, 4, 5, 6]
    [12, 9, 10, 4, 5, 6]
```

# Contar elementos de una Lista
```py
    c = [12,9,10]*2 + [4,5,6]

    print(c)
    print(c.count(12))
    print(c.count(4))
```
### Salida
```py
    [12, 9, 10, 4, 5, 6, 12, 9, 10, 4, 5, 6, 4, 5, 6]
    2
    1
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

# Slice Lista
- Slice 3 argumentos [desde:hasta:salto], por defecto salto tiene el valor 1
```py
    Lista original: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    Lista [:5:1] o [:5]: [0, 1, 2, 3, 4]
    Lista [:5:2]: [0, 2, 4]
    Lista [:5:2]: [0, 3]
```
### Ejemplo
```py
    vec = list(range(10))
    print(vec[:5])
```

# Inverir Lista
```py
    hola = [1,2,3]
    print(hola[::-1])
```
### Salida
```py
    [3, 2, 1]
```
# Sets
```py
    e = set(d)
    print(d)
    print(e)
    print({1,1,2,3,5,5})

    e.add(3)
    e.add(16)

    print(e)
```
### Salida
```py
    [1, 1, 2, 3, 5, 5]
    {1, 2, 3, 5}
    {1, 2, 3, 5}
    {1, 2, 3, 5, 16}
```

# Funciones lambda
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

    lb_condicional = lambda a: "par" if a%2==0 else "impar"

    print(sumar(2,2))
    print(sumar(2))
    print(lb_condicional(2))
```

# Funcion for de una linea
```py
    #Crea una lista de elementos [0, 0, 0, 3, 0, 0, 6, 0, 0, 9]
    for_condicional = [v if v%3==0 else 0 for v in range(10)]

    #Crea un generador iterable de 10 elementos, no una tupla
    generator = (v if v%3==0 else 0 for v in range(10))
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

# Iterable
__Los iterables son un conjunto de elemento que se pueden recorrer pero que una vez echo se consumen__

- Se pueden crear a travez del metodo iter(...) o con un generador

```py
    it = iter([...])
    gen = (random.randint(0, 100) for _ in range(2))

    print(next(gen))
    print(next(gen))
    print(next(gen))
```

### Salida
```py
    21
    49
    StopIteration
```

## Metodo next(iterable) obtiene el siguiente elemento
```py
    it = iter([1,2,3])
    print(next(it))
    next(it)
    print(next(it))

    #Obtener el primer valor que cumpla cierta condicion
    it = range(50)
    print(next((v fofor v iii it i v%7==0 andaandd v>15)))
```
### Salida
```py
    1
    3
    21
```

## Metodo tee(iterable) copia un iterable
```py
    from itertools import tee

    it = iter([1,2,3])

    cpy, it = tee(it)
```
## Metodo islice(iterable, stop) crea de un iterable hasta una cantidad especificada de elementos
```py
    from itertools import islice
    ls = [1,2,3,4,5,6]
    it = islice(ls, 3) 
    print(list(it))
```

### Salida
```py
    [1,2,3]
```

## Metodo reduce(func, iterable) aplica una funcion a un iterable reduciéndolo a un único valor
```py
    from functools import reduce
    ls = [1,2,3,4,5,6]
    print(reduce(lambda a,b: a+b, ls))
```

### Salida
```py
    21
```

# Generadores
__Es una forma de crear un iterador, este este cada vez que se intenta obtener un elemento lo genera y lo devuelve, permitiendo ahorrar memoria al no tener todos los elementos cargados de golpe__

```py
    import random
    def random_generator(limit):
        for _ in range(limit):
            yield random.randint(0, 100)
    
    print(list(random_generator(3)))
```

### Salida
```py
    [21, 36, 36]
```

## Yield From
__Retorna los valores generador por otro generador__

```py
    def yield_from():
        a = [1, 2, 3]
        b = "Hola"
        yield from a
        yield from b

    def random_cats(limit=3):
        yield from zip(get_cat(), random_generator(limit))

print(list(random_cats()))
print(list(yield_from()))
```
### Salida
```py
    [('Persa', 27), ('Siamés', 91), ('Maine Coon', 80)]
    [1, 2, 3, 'H', 'o', 'l', 'a']
```

# Funcion help
__Permite obtener la documentación de objetos como funciones, clases, módulos, variables, etc.__

```py
    help(print)
```

### Salida
```sh
    print(*args, sep=' ', end='\n', file=None, flush=False)
        Prints the values to a stream, or to sys.stdout by default.

        sep
        string inserted between values, default a space.
        end
        string appended after the last value, default a newline.
        file
        a file-like object (stream); defaults to the current sys.stdout.
        flush
        whether to forcibly flush the stream.
```