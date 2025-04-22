
from typing import Any, Callable, Iterator

#Imitacion de la funcion map
def _map(func: Callable[[Any], Any], iterable:Iterator)->Iterator: 
    for v in iter(iterable):
        yield func(v)

#Imitacion de la funcion filter
def _filter(func: Callable[[Any], Any], iterable:Iterator)->Iterator:
    for v in iter(iterable):
        if not func(v): continue
        yield v

_list = list(range(10))

print("Map")
for v in _map(lambda x:x**2, _list):
    print(v)

print("Filter")
for v in _filter(lambda x:x%5==0, _list):
    print(v)

print("Filter & Map")
for v in _filter(lambda x:x%5==0, _map(lambda x:x**2, _list)):
    print(v)
