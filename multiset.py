class MultiSet:
    def __init__(self):
        self._elements = {}

    def add(self, val):
        if val in self._elements:
            self._elements[val] += 1
        else:
            self._elements[val] = 1

    def remove(self, val):
        if val in self._elements:
            self._elements[val] -= 1
            if self._elements[val] == 0:
                del self._elements[val]

    def query(self, val):
        return val in self._elements

    def size(self):
        return sum(self._elements.values())