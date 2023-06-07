from datetime import datetime

class Nodo:
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

    def empty(self):
        if self._len == 0:
            return True

    def print(self):
        current = self._head
        resultado = ""
        while current._next != None:
            resultado = resultado + str(current._element) + "\t"
            current = current._next
        resultado = resultado + str(current._element) + "\t"
        print(resultado)

    def reverse_print(self):
        current = self._tail
        resultado = ""
        while current._prev != None:
            resultado = resultado + str(current._element) + "\t"
            current = current._prev
        resultado = resultado + str(current._element) + "\t"
        print(resultado)

    def shift(self, e):
        n = Nodo(e, None, None)
        if self.empty():
            self._head = n
            self._tail = n
        else:
            n._next = self._head
            self._head._prev = n
            self._head = n
        self._len += 1

    def append(self, e):
        n = Nodo(e, None, None)
        if self.empty():
            self._head = n
            self._tail = n
        else:
            n._prev = self._tail
            self._tail._next = n
            self._tail = n
        self._len += 1

    def add(self, e, pos):
        n = Nodo(e, None, None)
        if self.empty():
            self._head = n
            self._tail = n
            self._len += 1
        elif pos > len(self)+1:
            raise IndexError("Out of range")
        elif pos == 0:
            self.shift(e)
        elif pos == -1 or pos == len(self):
            self.append(e)
        else:
            contador = 1
            current = self._head
            while contador < pos:
                current = current._next
                contador += 1
            n._next = current._next
            n._prev = current
            current._next._prev = n 
            current._next = n
            self._len += 1

    def __getitem__(self, i):
        if -len(self) > i or i >= len(self):
            raise IndexError("Out of bounds")
        elif i >= 0:
            current = self._head
            while i > 0:
                current = current._next
                i -= 1
        elif i < 0:
            current = self._tail
            while i < -1:
                i += 1
                current = current._prev
        return current._element

