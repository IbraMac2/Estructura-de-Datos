import networkx as nx
import matplotlib.pyplot as plt
import random

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice, conexiones):
        self.vertices[vertice] = conexiones

    def obtener_costo(self, origen, destino):
        return self.vertices[origen][destino]

    def dibujar_grafo(self):
        G = nx.DiGraph()
        for origen, destinos in self.vertices.items():
            for destino, costo in destinos.items():
                G.add_edge(origen, destino, weight=costo)
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_size=5000, node_color='skyblue', font_size=12, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Grafo de los estados de la República Mexicana")
        plt.show()


grafo_estados = Grafo()
grafo_estados.agregar_vertice('Baja California', {'Sonora': 5, 'Baja California Sur': 3})
grafo_estados.agregar_vertice('Sonora', {'Baja California': 5, 'Chihuahua': 4})
grafo_estados.agregar_vertice('Baja California Sur', {'Baja California': 3, 'Sinaloa': 6})
grafo_estados.agregar_vertice('Chihuahua', {'Sonora': 4, 'Durango': 5})
grafo_estados.agregar_vertice('Sinaloa', {'Baja California Sur': 6, 'Durango': 4})
grafo_estados.agregar_vertice('Durango', {'Chihuahua': 5, 'Sinaloa': 4})


def recorrer_sin_repetir(inicio, grafo):
    visitados = set()
    visitados.add(inicio)
    actual = inicio
    camino = [inicio]
    costo_total = 0
    while len(visitados) < len(grafo.vertices):
        vecinos = grafo.vertices[actual]
        siguiente_estado = None
        min_costo = float('inf')
        for vecino, costo in vecinos.items():
            if vecino not in visitados and costo < min_costo:
                siguiente_estado = vecino
                min_costo = costo
        if siguiente_estado is None:
            break
        visitados.add(siguiente_estado)
        camino.append(siguiente_estado)
        costo_total += min_costo
        actual = siguiente_estado
    return camino, costo_total


def recorrer_con_repetir(inicio, grafo, veces):
    actual = inicio
    camino = [inicio]
    costo_total = 0
    for _ in range(veces):
        vecinos = list(grafo.vertices[actual].items())
        siguiente_estado, costo = random.choice(vecinos)
        camino.append(siguiente_estado)
        costo_total += costo
        actual = siguiente_estado
    return camino, costo_total


def dibujar_grafo():
    grafo_estados.dibujar_grafo()


while True:
    print("\nMenú:")
    print("1. Recorrer estados sin repetir")
    print("2. Recorrer estados permitiendo repetir")
    print("3. Dibujar grafo")
    print("4. Salir")

    opcion = int(input("Ingrese el número de la opción que desea realizar: "))

    if opcion == 1:
        inicio = 'Baja California'
        camino, costo_total = recorrer_sin_repetir(inicio, grafo_estados)
        print("Recorrido sin repetir estados:")
        print(camino)
        print("Costo total del recorrido:", costo_total)
    elif opcion == 2:
        inicio = 'Baja California'
        veces = int(input("Ingrese el número de veces que desea repetir estados: "))
        camino, costo_total = recorrer_con_repetir(inicio, grafo_estados, veces)
        print("Recorrido con repetir estados:")
        print(camino)
        print("Costo total del recorrido:", costo_total)
    elif opcion == 3:
        dibujar_grafo()
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
