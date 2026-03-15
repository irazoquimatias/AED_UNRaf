class Pila:
    def __init__(self):
        self._datos = []

    def __len__(self):
        return (len(self._datos))

    def vacio(self):
        if len(self._datos) == 0:
            return True
        else:
            return False

    def tope(self):
        return (self._datos[-1])

    def agregar(self, v):
        self._datos.append(v)

    def quitar(self):
        return self._datos.quitar()

    def imprimir(self):
        print(self._datos)

class Cola:
    def __init__(self):
        self._datos = []

    def __len__(self):
        return (len(self._datos))

    def vacio(self):
        if len(self._datos) == 0:
            return True
        else:
            return False

    def primero(self):
        return (self._datos[0])

    def agregar(self, v):
        self._datos.append(v)

    def quitar(self):
        return self._datos.quitar(0)

    def imprimir(self):
        print(self._datos)

