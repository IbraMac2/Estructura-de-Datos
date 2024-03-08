class Pila:
    def __init__(self, nombre):
        self.items = []
        self.nombre = nombre

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None


def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 desde {origen.nombre} hasta {destino.nombre}")
        destino.apilar(origen.desapilar())
    else:
        hanoi(n - 1, origen, auxiliar, destino)
        print(f"Mover disco {n} desde {origen.nombre} hasta {destino.nombre}")
        destino.apilar(origen.desapilar())
        hanoi(n - 1, auxiliar, destino, origen)



torre_inicial = Pila("Torre Inicial")
torre_auxiliar = Pila("Torre Auxiliar")
torre_final = Pila("Torre Final")

# Colocar los discos en la torre inicial
for disco in range(3, 0, -1):
    torre_inicial.apilar(disco)


print("Estado inicial:")
print(torre_inicial.nombre + ":", torre_inicial.items)
print(torre_auxiliar.nombre + ":", torre_auxiliar.items)
print(torre_final.nombre + ":", torre_final.items)
print("\nResolviendo...\n")


hanoi(3, torre_inicial, torre_final, torre_auxiliar)


print("\nEstado final:")
print(torre_inicial.nombre + ":", torre_inicial.items)
print(torre_auxiliar.nombre + ":", torre_auxiliar.items)
print(torre_final.nombre + ":", torre_final.items)
