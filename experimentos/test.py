from functools import reduce
ls = [1,2,3,4,5,6]
print(reduce(lambda a,b: a+b, ls))

lb_condicional = lambda a: "par" if a%2==0 else "impar"

for_condicional = [v if v%3==0 else 0 for v in range(10)]

print(for_condicional)