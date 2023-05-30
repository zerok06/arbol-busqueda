import random


def generateArr(num):
    arr = []
    for i in range(num):
        arr.append(random.randint(0, 100))

    return arr


def fillTree(arbol, arr):
    for i in range(len(arr)):
        arbol.insertar(arr[i])


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def insertar(self, valor):
        if self.valor:
            if valor < self.valor:
                if self.izquierda is None:
                    self.izquierda = Nodo(valor)
                else:
                    print(self.valor)
                    self.izquierda.insertar(valor)
            elif valor > self.valor:
                if self.derecha is None:
                    self.derecha = Nodo(valor)
                else:
                    print(self.valor)
                    self.derecha.insertar(valor)
        else:
            self.valor = valor

    def buscar(self, valor):
        if valor < self.valor:
            if self.izquierda is None:
                return str(valor) + " no encontrado"
            return self.izquierda.buscar(valor)
        elif valor > self.valor:
            if self.derecha is None:
                return str(valor) + " no encontrado"
            return self.derecha.buscar(valor)
        else:
            return str(self.valor) + " encontrado"


class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.raiz.insertar(valor)

    def buscar(self, valor):
        if self.raiz:
            print(self.raiz.valor)
            return self.raiz.buscar(valor)
        else:
            return "Árbol vacío"


arbol = Arbol()
arr = generateArr(20)
fillTree(arbol, arr)

print(arbol)
