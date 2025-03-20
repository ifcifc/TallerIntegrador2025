from typing import Iterable, Callable, Any
from functools import reduce
from itertools import tee, islice

class Stream:
    """
    Clase que imita el comportamiento de los streams de Java.
    Permite el procesamiento de colecciones de datos mediante operaciones encadenadas
    """
    __source: Iterable
    __iterator: Iterable

    def __init__(self, source:Iterable):
        """
        Inicializa un nuevo objeto Stream con la fuente de datos proporcionada.
        
        Args:
            source: Un iterable que servirá como fuente de datos para el stream
        """
        self.__source = iter(source)
        self.__iterator = None
    
    def __iter__(self):
        """
        Hace que la instancia de la clase sea iterable.

        Returns:
           El propio objeto Stream
        """
        return self

    def __next__(self):
        """
        Permite obtener el siguiente elemento del stream.
        
        Returns:
            El siguiente elemento del stream
            
        Raises:
            StopIteration: Cuando no hay más elementos
        """

        if self.__iterator is None:
            self.__iterator = iter(self.__source)
        try:
            return next(self.__iterator)
        except StopIteration as err:
            self.__iterator = None
            raise err

    def copy(self) -> 'Stream':
        """
        Crea una copia del stream actual.
        
        Returns:
            Un nuevo objeto Stream con los mismos elementos
        """
        cp, self.__source = tee(self.__source)
        return Stream(cp)
    
    def __copy__(self):
        """
        Implementa el protocolo de copia estándar de Python.
        
        Returns:
            Una copia del stream actual
        """
        return self.copy()

    #def convert_to_tuple(self) -> 'Stream':
    #    self.__source = tuple(self.__source)
    #    return self

    #def convert_to_iter(self) -> 'Stream':
    #    self.__source = iter(self.__source)
    #    return self

    def to_list(self) -> list:
        """
        Convierte el stream en una lista.
        
        Returns:
            Una lista con todos los elementos del stream
        """
        return list(self.__source)
    
    def to_tuple(self) -> tuple:
        """
        Convierte el stream en una tupla.
        
        Returns:
            Una tupla con todos los elementos del stream
        """
        return tuple(self.__source)

    def map(self, func: Callable[[Any], Any]) -> 'Stream':
        self.__source = map(func, self.__source)
        return self
    
    def filter(self, func: Callable[[Any], Any]) -> 'Stream':
        self.__source = filter(func, self.__source)
        return self
    
    def each(self, func: Callable[[Any], Any]) -> None:
        for item in self.__source:
            func(item)

    def peek(self, func: Callable[[Any], Any]) -> 'Stream':
        cp, self.__source = tee(self.__source)

        for v in cp:
            func(v)
        #funciona pero complicado
        #self.__source = iter(((v, func(v))[0] for v in self.__source))
        
        #no funciona
        #def generator():
        #    for v in self.__source:
        #        func(v)
        #        yield v
        #self.__source = generator()

        return self

    def reduce(self, func: Callable[[Any, Any], Any]) -> Any:
        return reduce(func, self.__source)

    def min(self, key: Callable[[Any], Any]=None) -> Any:
        return min(self.__source, key=key)
    
    def max(self, key: Callable[[Any], Any]=None) -> Any:
        return max(self.__source, key=key)
    
    def any(self, func: Callable[[Any], bool]=lambda v:v) -> bool:
        return any(func(v) for v in self.__source)
    
    def all(self, func: Callable[[Any], bool]=lambda v:v) -> bool:
        return all(func(v) for v in self.__source)
    
    def sort(self, key:Callable[[Any], Any]=None, reverse = False) -> 'Stream':
        self.__source = iter(sorted(self.__source, key=key, reverse=reverse))
        return self
    
    def reverse(self) -> 'Stream':
        self.__source = reversed(self.__source)
        return self

    def first(self, func: Callable[[Any], bool]=None)->Any:
        if func==None:
            return next(self.__source)
        else:
            return next((v for v in self.__source if func(v)))
    
    def last(self, func: Callable[[Any], bool]=None)->Any:
        if func==None:
            return next(reversed(tuple(self.__source)))
        else:
            return next((v for v in reversed(tuple(self.__source)) if func(v)))

    def limit(self, limit:int) -> 'Stream':
        self.__source = islice(self.__source, limit)
        return self


