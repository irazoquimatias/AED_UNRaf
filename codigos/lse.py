class Nodo:
	def __init__(self, e, n):
    	    self._element = e
    	    self._next = n

class LSE:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def __len__(self):
        return self._len

    def empty(self):
        if self._len == 0:
            return True

    def print(self):
        current = self._head
        resultado = ""
        while current._next != None:
            resultado = resultado + str(current._element) + "; "
            current = current._next
        resultado = resultado + str(current._element) + "; "
        print(resultado)

    def shift(self, e):
        n = Nodo(e, None)
        if self.empty():
            self._head = n
        else:
            n._next = self._head
            self._head = n
        self._len += 1

    def append(self, e):
        n = Nodo(e, None)
        if self.empty():
            self._head = n
        else:
            current = self._head
            while current._next != None:
                current = current._next
            current._next = n
        self._len += 1

    def append_tail(self, e):
        n = Nodo(e, None)
        if self.empty():
            self._head = n
            self._tail = n
        else:
            self._tail._next = n
            self._tail = n
        self._len += 1

    def unshift(self):
        if self.empty():
            raise IndexError ("Vacia")
        current = self._head
        self._head = self._head._next
        self._len -= 1
        return current._element

    def pop(self):
        if self.empty():
            raise IndexError ("Vacia")
        current = self._head
        while current._next != None:
            previous = current
            current = current._next
        previous._next = None
        self._size =- 1
        return current._element

    def remove(self, e):
        if self.empty():
            raise IndexError ("Vacia")
        while self._head._element == e:
            self.unshift()
        current = self._head
        while current._next != None:
            previous = current
            current = current._next
            while current._element == e:
                current = current._next
                previous._next = current
        self._size =- 1

    def remove_pos(self, p):
        if self.empty():
            raise IndexError ("Vacia")
        current = self._head
        contador = 1
        while contador < p:
            previous = current
            current = current._next
            contador += 1
        previous._next = current._next
        self._size =- 1        

    def __getitem__(self, i):
        if self.empty():
            raise IndexError ("Vacia")
        contador = 1
        current = self._head
        while i > 0:
            current = current._next
            i -= 1
        return current._element

