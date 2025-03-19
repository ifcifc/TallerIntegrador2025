# Multiplicar STR
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
