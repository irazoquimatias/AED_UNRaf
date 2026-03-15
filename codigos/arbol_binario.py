import random

class Nodo:
    def __init__(self,e):
        self._elemento = e
        self._padre = None
        self._izquierda = None
        self._derecha = None

class ArbolBinario:
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
    
    def is_hoja(self, n):
        if n._derecha == None and n._izquierda == None:
            return True

    def padre(self, n):
        if es_raiz(n):
            raise IndexError("n es el nodo raiz")
        return n._padre

    def izquierda(self, n):
        return n._izquierda

    def derecha(self, n):
        return n._derecha

    def agregar(self, e, n=None):
        if self.vacio():
            n = Nodo(e)
            self._raiz = n
            self._tamano += 1
        
        if n == None and not self.vacio():
            n = self._raiz

        if e < n._elemento and n._izquierda != None:
            self.agregar(e, n._izquierda)
        elif e < n._elemento and n._izquierda == None:
            nuevo = Nodo(e)
            nuevo._padre = n
            n._izquierda = nueva
            self._tamano += 1
        elif e > n._elemento and n._derecha != None:
            self.agregar(e, n._derecha)
        elif e > n._elemento and n._derecha == None:
            nueva = Nodo(e)
            nueva._padre = n
            n._derecha = nueva
            self._tamano += 1

    def profundidad(self, n):
        if es_raiz(n):
            return 0
        else:
            return 1 + profundidad(n._padre)

    def altura(self, n):
        if self.is_hoja(n):
            return 0
        elif n._izquierda == None:
            return 1 + self.altura(n._derecha)
        elif n._derecha == None:
            return 1 + self.altura(n._izquierda)
        elif self.altura(n._izquierda) > self.altura(n._derecha):
            return 1 + self.altura(n._izquierda)
        else:
            return 1 + self.altura(n._derecha)

    def preorder(self, l = None, n = None):
        if n == None:
            n = self._raiz
            l = []

        l.append(n._elemento)
        if n._izquierda != None:
            self.preorder(l, n._izquierda) 
        if n._derecha != None:
            self.preorder(l, n._derecha)

    def inorder(self, l = None, n = None):
        if n == None:
            n = self._raiz
            l = []

        if n._izquierda != None:
            self.inorder(l, n._izquierda) 
        l.append(n._elemento)
        if n._derecha != None:
            self.inorder(l, n._derecha)

    def postorder(self, l = None, n = None):
        if n == None:
            n = self._raiz
            l = []

        if n._izquierda != None:
            self.postorder(l, n._izquierda) 
        if n._derecha != None:
            self.postorder(l, n._derecha)
        l.append(n._elemento)

    def anchura(self, l):
        cola = []
        cola.append(self._raiz)
        while len(cola) > 0:
            n = cola.pop(0)
            l.append(n._elemento)
            if n._izquierda != None:
                cola.append(n._izquierda)
            if n._derecha != None:
                cola.append(n._derecha)

    def camino(self, f, c = None, nodo=None):
        if nodo == None:
            nodo = self._raiz
            c = ""

        c = c + "\t" + str(nodo._elemento)
        if nodo._elemento == f:
            print (c)
        elif nodo._elemento < f:
            nodo = self.derecha(nodo)
            self.camino(f, c, nodo)
        else:
            nodo = self.izquierdat(nodo)
            self.camino(f, c, nodo)

    def lca(self, a, b):
        ancestros_a = []
        ancestros_b = []
        nodo = self.raiz()
        while nodo._elemento != a:
            ancestros_a.append(nodo._elemento)
            if nodo._elemento > a:
                nodo = nodo._izquierda
            else:
                nodo = nodo._derecha
        nodo = self._raiz
        while nodo._elemento != b:
            ancestros_b.append(nodo._elemento)
            if nodo._elemento > b:
                nodo = nodo._izquierda
            else:
                nodo = nodo._derecha

        for i in range(len(ancestros_a)-1, -1, -1):
            for j in range(len(ancestros_b)-1, -1, -1):
                if ancestros_b[j] == ancestros_a[i]:
                    return ancestros_b[j]

