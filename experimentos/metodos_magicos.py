class test:
    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return f"Valor: {self.valor}"

    def __add__(self, other):
        return test(self.valor + other.valor)

    def __sub__(self, other):
        return test(self.valor - other.valor)

    def __call__(self, value):
        return test(self.valor + value)
    
    def __eq__(self, other):
        return self.valor == other.valor
    
    def __lt__(self, other):
        return self.valor < other.valor
    
    def __le__(self, other):
        return self.valor <= other.valor

test1 = test(10)
test2 = test(5)

print(test1 + test2) # Valor: 15
print(test1 - test2) # Valor: 5
print(test1(30)) # Valor: 40

print(test1 == test2) # False
print(test1 > test2) # False
print(test1 <= test2) # False
print(test1 <= test2(5)) # True
print(test1 < test2(15)) # True
