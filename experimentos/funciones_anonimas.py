sumar = lambda a, b=0: a + b

print(sumar(2,2))
print(sumar(2))


isOn:bool = False
def set_on(v:bool):
    global isOn
    isOn = v

toggle =  lambda : (set_on(not isOn), isOn)[1]

#No funciona
#toggle =  lambda : isOn = not IsOn

print("On?: ", toggle())
print("On?: ", toggle())
print("On?: ", toggle())