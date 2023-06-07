import random

class Nodo:
    def __init__(self,e):
        self._element = e
        self._parent = None
        self._left = None
        self._right = None

class ArbolBinario:
    def __init__(self):
        self._root = None
        self._size = 0
        
    def __len__(self):
        return self._size

    def is_empty(self):
        if len(self) == 0:
            return True

    def root(self):
        return self._root

    def is_root(self, n):
        if n._parent == None:
            return True
    
    def is_leaf(self, n):
        if n._right == None and n._left == None:
            return True

    def parent(self, n):
        if is_root(n):
            raise IndexError("n es el nodo raiz")
        return n._parent

    def left(self, n):
        return n._left

    def right(self, n):
        return n._right

    def add(self, e, n=None):
        if self.is_empty():
            n = Nodo(e)
            self._root = n
            self._size += 1
        
        if n == None and not self.is_empty():
            n = self._root

        if e < n._element and n._left != None:
            self.add(e, n._left)
        elif e < n._element and n._left == None:
            new = Nodo(e)
            new._parent = n
            n._left = new
            self._size += 1
        elif e > n._element and n._right != None:
            self.add(e, n._right)
        elif e > n._element and n._right == None:
            new = Nodo(e)
            new._parent = n
            n._right = new
            self._size += 1

    def depth(self, n):
        if is_root(n):
            return 0
        else:
            return 1 + depth(n._parent)

    def height(self, n):
        if self.is_leaf(n):
            return 0
        elif n._left == None:
            return 1 + self.height(n._right)
        elif n._right == None:
            return 1 + self.height(n._left)
        elif self.height(n._left) > self.height(n._right):
            return 1 + self.height(n._left)
        else:
            return 1 + self.height(n._right)

    def preorder(self, l, n = None):
        if n == None:
            n = self._root

        l.append(n._element)
        if n._left != None:
            self.preorder(l, n._left) 
        if n._right != None:
            self.preorder(l, n._right)

    def inorder(self, l, n = None):
        if n == None:
            n = self._root

        if n._left != None:
            self.inorder(l, n._left) 
        l.append(n._element)
        if n._right != None:
            self.inorder(l, n._right)

    def postorder(self, l, n = None):
        if n == None:
            n = self._root

        if n._left != None:
            self.postorder(l, n._left) 
        if n._right != None:
            self.postorder(l, n._right)
        l.append(n._element)

    def breadth_first(self, l):
        cola = []
        cola.append(self._root)
        while len(cola) > 0:
            n = cola.pop(0)
            l.append(n._element)
            if n._left != None:
                cola.append(n._left)
            if n._right != None:
                cola.append(n._right)

    def camino(self, f, c = None, nodo=None):
        if nodo == None:
            nodo = self._root
            c = ""

        c = c + "\t" + str(nodo._element)
        if nodo._element == f:
            print (c)
        elif nodo._element < f:
            nodo = self.right(nodo)
            self.camino(f, c, nodo)
        else:
            nodo = self.leftt(nodo)
            self.camino(f, c, nodo)

    def lca(self, a, b):
        ancestros_a = []
        ancestros_b = []
        nodo = self.root()
        while nodo._element != a:
            ancestros_a.append(nodo._element)
            if nodo._element > a:
                nodo = nodo._left
            else:
                nodo = nodo._right
        nodo = self._root
        while nodo._element != b:
            ancestros_b.append(nodo._element)
            if nodo._element > b:
                nodo = nodo._left
            else:
                nodo = nodo._right

        for i in range(len(ancestros_a)-1, -1, -1):
            for j in range(len(ancestros_b)-1, -1, -1):
                if ancestros_b[j] == ancestros_a[i]:
                    return ancestros_b[j]

