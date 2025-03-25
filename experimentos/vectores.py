vec = list(range(10))

#Slice 3 argumentos [desde:hasta:salto], por defecto salto tiene el valor 1
print("Slice")
print("Vector original:", vec)
print("Vector [:5:1] o [:5]:", vec[:5])
print("Vector [:5:2]:", vec[:5:2])
print("Vector [:5:3]:", vec[:5:3])

a = [12,9,10]
b = [4,5,6]
c = a + b
a.extend(b)
print(a)
print(c)

d = a*2 + b

print( d.count(12))

print(c.count(4))