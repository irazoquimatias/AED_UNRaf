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

    def print(self):
        to_visit = [self._root]
        while len(to_visit) > 0:
            current = to_visit.pop(0)
            to_visit += current._children
            print (current._element)
        
    def linaje(self, e):
        to_visit = [self._root]
        current = self._root
        while current._element != e and len(to_visit) > 0:
            to_visit += current._children
            current = to_visit.pop(0)

        if current._element != e:
            raise ValueError("No esta, amiguito")
        lin = []
        while current != self._root:
            lin = [current._element] + lin
            current = current._parent
        lin = [current._element] + lin
        return lin

if __name__ == "__main__":
    animales = ArbolNoBinario()
    animales.add("Metazoa")
    animales.add("Characiformes", "Metazoa")
    animales.add("Acestrorhynchidae", "Characiformes")
    animales.add("Acestrorhynchus", "Acestrorhynchidae")
    animales.add("Acestrorhynchus", "Acestrorhynchus pantaneiro")
    animales.add("Actinopterygii", "Metazoa")
    animales.add("Characiformes", "Actinopterygii")
    animales.add("Characidae", "Characiformes")
    animales.add("Oligosarcus", "Characidae")
    animales.add("Oligosarcus hepsetus", "Oligosarcus")
    animales.add("Actinopterygii", "Metazoa")
    animales.add("Characidae", "Actinopterygii")
    animales.add("Roeboides", "Characidae")
    animales.add("Roeboides descalvadensis", "Roeboides")
    animales.add("Aves", "Metazoa")
    animales.add("Passeriformes", "Aves")
    animales.add("Pipridae", "Passeriformes")
    animales.add("Chiroxiphia", "Pipridae")
    animales.add("Chiroxiphia caudata", "Chiroxiphia")
    animales.add("Aves", "Metazoa")
    animales.add("Passeriformes", "Aves")
    animales.add("Pipridae", "Passeriformes")
    animales.add("Manacus", "Pipridae")
    animales.add("Manacus manacus", "Manacus")
    animales.add("Aves", "Metazoa")
    animales.add("Passeriformes", "Aves")
    animales.add("Pipridae", "Passeriformes")
    animales.add("Pipra", "Pipridae")
    animales.add("Pipra fasciicauda", "Pipra")
    animales.add("Mammalia", "Metazoa")
    animales.add("Carnivora", "Mammalia")
    animales.add("Felidae", "Carnivora")
    animales.add("Panthera", "Felidae")
    animales.add("Panthera onca", "Panthera")


    print(len(animales))
    animales.print()
    print(animales.linaje("Panthera onca"))
