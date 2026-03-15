class Nodo:
	def __init__(self, e, n):
    	    self._elemento = e
    	    self._siguiente = n

class LSE:
    def __init__(self):
        self._cabeza = None
        self._tamano = 0

    def __len__(self):
        return self._tamano

    def vacio   (self):
        if self._tamano == 0:
            return True

    def imprimir(self):
        actual = self._cabeza
        resultado = ""
        while actual._siguiente != None:
            resultado = resultado + str(actual._elemento) + "; "
            actual = actual._siguiente
        resultado = resultado + str(actual._elemento) + "; "
        print(resultado)

    def agregar_inicio(self, e):
        n = Nodo(e, None)
        if self.vacio():
            self._cabeza = n
        else:
            n._siguiente = self._cabeza
            self._cabeza = n
        self._tamano += 1

    def agregar_final(self, e):
        n = Nodo(e, None)
        if self.vacio():
            self._cabeza = n
        else:
            actual = self._cabeza
            while actual._siguiente != None:
                actual = actual._siguiente
            actual._siguiente = n
        self._tamano += 1

    def quitar_inicio(self):
        if self.vacio():
            raise IndexError ("Vacia")
        actual = self._cabeza
        self._cabeza = self._cabeza._siguiente
        self._tamano -= 1
        return actual._elemento

    def quitar_final(self):
        if self.vacio():
            raise IndexError ("Vacia")
        actual = self._cabeza
        while actual._siguiente != None:
            anterior = actual
            actual = actual._siguiente
        anterior._siguiente = None
        self._tamano =- 1
        return actual._elemento

    def quitar_valor(self, e):
        if self.vacio():
            raise IndexError ("Vacia")
        while self._cabeza._elemento == e:
            self.quitar_inicio()
        actual = self._cabeza
        while actual._siguiente != None:
            anterior = actual
            actual = actual._siguiente
            while actual._elemento == e:
                actual = actual._siguiente
                anterior._siguiente = actual
        self._tamano =- 1

    def quitar_posicion(self, p):
        if self.vacio():
            raise IndexError ("Vacia")
        actual = self._cabeza
        contador = 1
        while contador < p:
            anterior = actual
            actual = actual._siguiente
            contador += 1
        anterior._siguiente = actual._siguiente
        self._tamano =- 1        

    def __getitem__(self, i):
        if self.vacio():
            raise IndexError ("Vacia")
        contador = 1
        actual = self._cabeza
        while i > 0:
            actual = actual._siguiente
            i -= 1
        return actual._elemento

