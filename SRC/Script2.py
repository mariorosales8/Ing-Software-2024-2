def caminante(recorrido):
    altura = 0
    montañas = 0
    valles = 0
    for i in recorrido:
        if i == "U":
            altura += 1
            if altura == 0:
                valles += 1
        elif i == "D":
            altura -= 1
            if altura == 0:
                montañas += 1
    return valles

class arbol:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

    def agregar(self, valor):
        if valor <= self.valor:
            if self.izq is None:
                self.izq = arbol(valor)
            else:
                self.izq.agregar(valor)
        else:
            if self.der is None:
                self.der = arbol(valor)
            else:
                self.der.agregar(valor)

    def preorden(self):
        orden = []
        orden.append(self.valor)
        if self.izq:
            orden.extend(self.izq.preorden())
        if self.der:
            orden.extend(self.der.preorden())
        return orden

    def inorden(self):
        orden = []
        if self.izq:
            orden.extend(self.izq.inorden())
        orden.append(self.valor)
        if self.der:
            orden.extend(self.der.inorden())
        return orden

    def postorden(self):
        orden = []
        if self.izq:
            orden.extend(self.izq.postorden())
        if self.der:
            orden.extend(self.der.postorden())
        orden.append(self.valor)
        return orden

a = arbol(10)
a.agregar(5)
a.agregar(15)
a.agregar(3)
a.agregar(7)
a.agregar(13)

print(a.preorden())
print(a.inorden())
print(a.postorden())
