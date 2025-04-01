potencias_dict = {}

for i in range(1, 4):
    potencias_dict[str(i)] = i ** 2

print(potencias_dict)
print(f"La potencia de 3 es {potencias_dict['3']}")


def_dict = {
    "val1": "valor1",
    "val2": {
        "val3": "valor3",
        "val4": [1,2,3]
    }
}

print(def_dict)
print(def_dict["val2"]["val4"][1])