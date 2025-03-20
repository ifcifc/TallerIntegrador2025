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
        """
        Aplica una función a cada elemento del stream.
        
        Args:
            func: Función que recibe un elemento y devuelve un nuevo valor
            
        Returns:
            El mismo stream
        """
        
        self.__source = map(func, self.__source)
        return self
    
    def filter(self, predicate: Callable[[Any], Any]) -> 'Stream':
        """
        Filtra los elementos del stream según una función predicado.
        
        Args:
            predicate: Función que recibe un elemento y devuelve un booleano
            
        Returns:
            El mismo stream
        """

        self.__source = filter(predicate, self.__source)
        return self
    
    def each(self, func: Callable[[Any], Any]) -> None:
        """
        Aplica una función a cada elemento del stream como efecto secundario.
        
        Args:
            func: Función que recibe un elemento y realiza alguna acción
        """
        for item in self.__source:
            func(item)

    def peek(self, func: Callable[[Any], Any]) -> 'Stream':
        """
        Aplica una función a cada elemento sin modificar el stream.
        
        Args:
            func: Función que recibe un elemento y realiza alguna acción
            
        Returns:
            El mismo stream
        """
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
        """
        Reduce el stream a un único valor aplicando una función de acumulación.
        
        Args:
            func: Función que recibe dos elementos y devuelve un resultado
            
        Returns:
            El valor resultante de la reducción
        """
        return reduce(func, self.__source)

    def min(self, key: Callable[[Any], Any]=None) -> Any:
        """
        Obtiene el elemento mínimo del stream.
        
        Args:
            key: Función opcional para extraer un valor de comparación
            
        Returns:
            El elemento mínimo del stream
        """
        return min(self.__source, key=key)
    
    def max(self, key: Callable[[Any], Any]=None) -> Any:
        """
        Obtiene el elemento maximo del stream.
        
        Args:
            key: Función opcional para extraer un valor de comparación
            
        Returns:
            El elemento maximo del stream
        """
        return max(self.__source, key=key)
    
    def any(self, predicate: Callable[[Any], bool]=lambda v:v) -> bool:
        """
        Comprueba si algún elemento del stream cumple con el predicado.
        
        Args:
            predicate: Función predicado, por defecto usa el valor del elemento
            
        Returns:
            True si al menos un elemento cumple la condición, False en caso contrario
        """
        return any(predicate(v) for v in self.__source)
    
    def all(self, predicate: Callable[[Any], bool]=lambda v:v) -> bool:
        """
        Comprueba si todos los elementos del stream cumplen con el predicado.
        
        Args:
            predicate: Función predicado, por defecto usa el valor del elemento
            
        Returns:
            True si todos los elementos cumplen la condición, False en caso contrario
        """
        return all(predicate(v) for v in self.__source)
    
    def sort(self, key:Callable[[Any], Any]=None, reverse = False) -> 'Stream':
        """
        Ordena los elementos del stream.
        
        Args:
            key: Función opcional para extraer un valor de comparación
            reverse: Si es True, ordena en orden descendente
            
        Returns:
            El mismo stream
        """
        self.__source = iter(sorted(self.__source, key=key, reverse=reverse))
        return self
    
    def reverse(self) -> 'Stream':
        """
        Invierte el orden de los elementos del stream.
        
        Returns:
            El mismo stream
        """
        self.__source = reversed(tuple(self.__source))
        return self

    def first(self, predicate: Callable[[Any], bool]=None)->Any:
        """
        Obtiene el primer elemento del stream o el primer elemento que cumpla el predicado.
        
        Args:
            predicate: Función predicado opcional
            
        Returns:
            El primer elemento que cumpla la condición o 
            el primer elemento si no se proporciona función
        """
        if predicate is None:
            return next(self.__source)
        else:
            return next((v for v in self.__source if predicate(v)))
    
    def last(self, predicate: Callable[[Any], bool]=None)->Any:
        """
        Obtiene el último elemento del stream o el último elemento que cumpla el predicado.
        
        Args:
            predicate: Función predicado opcional
            
        Returns:
            El último elemento que cumpla la condición o 
            el último elemento si no se proporciona función
        """
        if predicate is None:
            return next(reversed(tuple(self.__source)))
        else:
            return next((v for v in reversed(tuple(self.__source)) if predicate(v)))

    def limit(self, limit:int) -> 'Stream':
        """
        Limita el número de elementos del stream.
        
        Args:
            limit: Número máximo de elementos a mantener
            
        Returns:
            El mismo stream
        """
        self.__source = islice(self.__source, limit)
        return self

    def count(self, predicate: Callable[[Any], bool]=lambda v: True)->int:
        """
        Cuenta el número total de elementos en el stream o 
        el número total de elementos que cumplan con el predicado.

        Args:
            predicate: Función predicado opcional

        Returns:
            El número de elementos en el stream
        """
        cp, self.__source = tee(self.__source)

        return sum(1 for _ in cp if predicate(cp))