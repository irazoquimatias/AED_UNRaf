class Nodo:
    def __init__(self,e):
        self._element = e
        self._parent = None
        self._children = []

class ArbolNoBinario:
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
        if n._children == []:
            return True

    def parent(self, n):
        if is_root(n):
            raise IndexError("n es el nodo raiz")
        return n._parent

    def depth(self, n):
        if is_root(n):
            return 0
        else:
            return 1 + depth(n._parent)

    def add(self, e, p=None):
        n = Nodo(e)
        if p == None:
            self._root = n
            self._size += 1
        else:
            to_visit = [self._root]
            current = self._root
            while current._element != p and len(to_visit) > 0:
                to_visit += current._children
                current = to_visit.pop(0)

            added = False
            for c in current._children:
                if c._element == n._element:
                    added = True
            if not added:
                current._children.append(n)
                n._parent = current
                self._size += 1
