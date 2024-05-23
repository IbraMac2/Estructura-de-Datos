def busqueda_hash(lista, objetivo):
    tabla_hash = {valor: indice for indice, valor in enumerate(lista)}
    if objetivo in tabla_hash:
        return tabla_hash[objetivo]
    return -1

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
objetivo = 9
resultado = busqueda_hash(numeros, objetivo)

if resultado != -1:
    print(f'El número {objetivo} se encuentra en el índice {resultado}.')
else:
    print(f'El número {objetivo} no está en la lista.')





def busqueda_hash_cadenas(lista, objetivo):
    tabla_hash = {valor: indice for indice, valor in enumerate(lista)}
    if objetivo in tabla_hash:
        return tabla_hash[objetivo]
    return -1

cadenas = ["manzana", "banana", "cereza", "durazno", "kiwi", "mango"]
objetivo = "cereza"
resultado = busqueda_hash_cadenas(cadenas, objetivo)

if resultado != -1:
    print(f'La cadena "{objetivo}" se encuentra en el índice {resultado}.')
else:
    print(f'La cadena "{objetivo}" no está en la lista.')
