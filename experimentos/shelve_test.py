import shelve

#Funciona como un diccionario, pero almacena los datos en disco
with shelve.open('dict.shelve') as dic:
    if '888' not in dic:
        for i in range(1, 9999):
            dic[str(i)] = i ** 2
        
    print(dic['888'])