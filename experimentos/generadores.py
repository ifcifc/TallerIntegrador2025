import random

def get_cat():
    cats = ["Persa","Siamés","Maine Coon","Bengala","Ragdoll","Británico de pelo corto","Esfinge","Abisinio","Scottish Fold","Siberiano"]
    for cat in cats:
        yield cat



def random_generator(limit):
    for _ in range(limit):
        yield random.randint(0, 100)

def random_cats(limit=3):
    yield from zip(get_cat(), random_generator(limit))

def yield_from():
    a = [1, 2, 3]
    b = "Hola"
    yield from a
    yield from b

print(next(get_cat()))

print(list(random_generator(3)))
print(list(random_cats()))
print(list(yield_from()))