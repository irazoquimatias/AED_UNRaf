class Pila:
    def __init__(self):
        self._data = []

    def __len__(self):
        return (len(self._data))

    def empty(self):
        if len(self._data) == 0:
            return True
        else:
            return False

    def top(self):
        return (self._data[-1])

    def push(self, v):
        self._data.append(v)

    def pop(self):
        return self._data.pop()

    def print(self):
        print(self._data)

class Cola:
    def __init__(self):
        self._data = []

    def __len__(self):
        return (len(self._data))

    def empty(self):
        if len(self._data) == 0:
            return True
        else:
            return False

    def first(self):
        return (self._data[0])

    def enqueue(self, v):
        self._data.append(v)

    def dequeue(self):
        return self._data.pop(0)

    def print(self):
        print(self._data)

