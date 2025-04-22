
from numbers import Number
from typing import Any, Callable, Iterator, Optional

#Imitacion de la funcion map
def _map(func: Callable[[Any], Any], iterable:Iterator)->Iterator: 
    for v in iterable:
        yield func(v)

#Imitacion de la funcion filter
def _filter(func: Callable[[Any], Any], iterable:Iterator)->Iterator:
    for v in iterable:
        if not func(v): continue
        yield v

#Imitacion de la funcion max
def _max(iterable:Iterator, key:Optional[Callable[[Any], Number]]=None, default=0)->object:
    max_value:Number = None
    max_obj:object = None#Objeto retornado 
    for v in iterable:
        #Si no se define una funcion para key se usa el valor del iterable
        value = v if key==None else key(v)
        #Si max_value es none significa que es el primer bucle y lo inicializa
        if max_value==None or value>max_value:
            max_value = value        
            max_obj = v

    return max_obj or default

_list = list(range(10))
_list_obj = [
    {
        "name": f"name_{i}",
        "value": i**3
    } for i in range(10)
]


print("Map")
for v in _map(lambda x:x**2, _list):
    print(v)

print("Filter")
for v in _filter(lambda x:x%5==0, _list):
    print(v)

print("Filter & Map")
for v in _filter(lambda x:x%5==0, _map(lambda x:x**2, _list)):
    print(v)

print("Max")
print(_max(_list_obj, key=lambda x: x["value"]))
print(_max(_list))
print(_max([]))
