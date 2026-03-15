from datetime import datetime

class Nodo:
	def __init__(self, e, s, a):
    	    self._elemento = e
    	    self._siguiente = n
    	    self._anterior = p

class LDE:
    def __init__(self):
        self._cabeza = None
        self._cola = None
        self._tamano = 0

    def __len__(self):
        return self._tamano

    def vacio(self):
        if self._tamano == 0:
            return True

    def imprimir(self):
        actual = self._cabeza
        resultado = ""
        while actual._siguiente != None:
            resultado = resultado + str(actual._elemento) + "\t"
            actual = actual._siguiente
        resultado = resultado + str(actual._elemento) + "\t"
        print(resultado)

    def imprimir_reverso(self):
        actual = self._cola
        resultado = ""
        while actual._anterior != None:
            resultado = resultado + str(actual._elemento) + "\t"
            actual = actual._anterior
        resultado = resultado + str(actual._elemento) + "\t"
        print(resultado)

    def agregar_inicio(self, e):
        n = Nodo(e, None, None)
        if self.vacio():
            self._cabeza = n
            self._cola = n
        else:
            n._siguiente = self._cabeza
            self._cabeza._anterior = n
            self._cabeza = n
        self._tamano += 1

    def agregar_final(self, e):
        n = Nodo(e, None, None)
        if self.vacio():
            self._cabeza = n
            self._cola = n
        else:
            n._anterior = self._cola
            self._cola._siguiente = n
            self._cola = n
        self._tamano += 1

    def agregar(self, e, pos):
        n = Nodo(e, None, None)
        if self.vacio():
            self._cabeza = n
            self._cola = n
            self._tamano += 1
        elif pos > len(self)+1:
            raise IndexError("Out of range")
        elif pos == 0:
            self.agregar_inicio(e)
        elif pos == -1 or pos == len(self):
            self.agregar_final(e)
        else:
            contador = 1
            actual = self._cabeza
            while contador < pos:
                actual = actual._siguiente
                contador += 1
            n._siguiente = actual._siguiente
            n._anterior = actual
            actual._siguiente._anterior = n 
            actual._siguiente = n
            self._tamano += 1

    def __getitem__(self, i):
        if -len(self) > i or i >= len(self):
            raise IndexError("Out of bounds")
        elif i >= 0:
            actual = self._cabeza
            while i > 0:
                actual = actual._siguiente
                i -= 1
        elif i < 0:
            actual = self._cola
            while i < -1:
                i += 1
                actual = actual._anterior
        return actual._elemento

