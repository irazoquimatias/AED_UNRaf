class Pila:
    def __init__(self):
        self._data = []

    def __len__(self):
        return (len(self._data))

    def agregar(self, v):
        self._data.append(v)    

    def quitar(self):
        return self._data.pop()

class Cola:
    def __init__(self):
        self._data = []

    def __len__(self):
        return (len(self._data))

    def agregar(self, v):
        self._data.append(v)

    def quitar(self):
        return self._data.pop(0)

class NodoLSE:
	def __init__(self, e, n):
    	    self._element = e
    	    self._next = n
class LSE:
    def __init__(self):
        self._head = None
        self._len = 0

    def __len__(self):
        return self._len

    def agregar_inicio(self, e):
        n = NodoLSE(e, None)
        if len(self) == 0:
            self._head = n
        else:
            n._next = self._head
            self._head = n
        self._len += 1

    def agregar_final(self, e):
        n = NodoLSE(e, None)
        if len(self) == 0:
            self._head = n
        else:
            current = self._head
            while current._next != None:
                current = current._next
            current._next = n
        self._len += 1

class NodoLDE:
	def __init__(self, e, n, p):
    	    self._element = e
    	    self._next = n
    	    self._prev = p

class LDE:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def __len__(self):
        return self._len

    def agregar_inicio(self, e):
        n = NodoLDE(e, None, None)
        if len(self) == 0:
            self._head = n
            self._tail = n
        else:
            n._next = self._head
            self._head._prev = n
            self._head = n
        self._len += 1

    def agregar_final(self, e):
        n = NodoLDE(e, None, None)
        if len(self) == 0:
            self._head = n
            self._tail = n
        else:
            n._prev = self._tail
            self._tail._next = n
            self._tail = n
        self._len += 1

class NodoArbolBinario:
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

    def agregar(self, e, n=None):
        if self.is_empty():
            n = NodoArbolBinario(e)
            self._root = n
            self._size += 1

        if n == None and not len(self) == 0:
            n = self._root

        if e < n._element and n._left != None:
            self.agregar(e, n._left)
        elif e < n._element and n._left == None:
            new = NodoArbolBinario(e)
            new._parent = n
            n._left = new
            self._size += 1
        elif e > n._element and n._right != None:
            self.agregar(e, n._right)
        elif e > n._element and n._right == None:
            new = NodoArbolBinario(e)
            new._parent = n
            n._right = new
            self._size += 1

