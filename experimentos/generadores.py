import random

def get_cat():
    cats = ["Persa","Siamés","Maine Coon","Bengala","Ragdoll","Británico de pelo corto","Esfinge","Abisinio","Scottish Fold","Siberiano"]
    for cat in cats:
        yield cat



def random_generator(limit):
    for _ in range(limit):
        yield random.randint(0, 100)

print(next(get_cat()))

print(list(random_generator(3)))