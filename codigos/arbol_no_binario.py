class Nodo:
    def __init__(self,e):
        self._elemento = e
        self._padre = None
        self.hijos = []

class ArbolNoBinario:
    def __init__(self):
        self._raiz = None
        self._tamano = 0
        
    def __len__(self):
        return self._tamano

    def vacio(self):
        if len(self) == 0:
            return True

    def raiz(self):
        return self._raiz

    def es_raiz(self, n):
        if n._padre == None:
            return True
    
    def es_hoja(self, n):
        if n.hijos == []:
            return True

    def padre(self, n):
        if es_raiz(n):
            raise IndexError("n es el nodo raiz")
        return n._padre

    def profundidad(self, n):
        if es_raiz(n):
            return 0
        else:
            return 1 + profundidad(n._padre)

    def agregar(self, e, p=None):
        n = Nodo(e)
        if p == None:
            self._raiz = n
            self._tamano += 1
        else:
            por_visitar = [self._raiz]
            actual = self._raiz
            while actual._elemento != p and len(por_visitar) > 0:
                por_visitar += actual.hijos
                actual = por_visitar.pop(0)

            agregado = False
            for c in actual.hijos:
                if c._elemento == n._elemento:
                    agregado = True
            if not agregado:
                actual.hijos.append(n)
                n._padre = actual
                self._tamano += 1
