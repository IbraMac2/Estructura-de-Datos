class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijo_izquierdo = None
        self.hijo_derecho = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(valor, self.raiz)

    def _agregar_recursivo(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.hijo_izquierdo is None:
                nodo.hijo_izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo.hijo_izquierdo)
        else:
            if nodo.hijo_derecho is None:
                nodo.hijo_derecho = Nodo(valor)
            else:
                self._agregar_recursivo(valor, nodo.hijo_derecho)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(valor, nodo.hijo_izquierdo)
        else:
            return self._buscar_recursivo(valor, nodo.hijo_derecho)


arbol = Arbol()
arbol.agregar(5)
arbol.agregar(3)
arbol.agregar(7)
arbol.agregar(2)
arbol.agregar(4)
arbol.agregar(6)
arbol.agregar(8)

print(arbol.buscar(4))
print(arbol.buscar(9))
