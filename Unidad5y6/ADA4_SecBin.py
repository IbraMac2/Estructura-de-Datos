def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
objetivo = 5
resultado = busqueda_secuencial(numeros, objetivo)

if resultado != -1:
    print(f'El número {objetivo} se encuentra en el lugar {resultado}.')
else:
    print(f'El número {objetivo} no está en la lista.')






def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

numeros_ordenados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
objetivo = 7
resultado = busqueda_binaria(numeros_ordenados, objetivo)

if resultado != -1:
    print(f'El número {objetivo} se encuentra en el lugar {resultado}.')
else:
    print(f'El número {objetivo} no está en la lista.')




