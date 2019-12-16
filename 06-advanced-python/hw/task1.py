"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""


class Graph_iter:
    def __init__(self, collection, pointer):
        self._collection = collection
        self._pointer = pointer
        self.v = ''
        self._vr = []
        self.used = []

    def __next__(self):
        if not self._pointer:
            keys = list(self._collection.keys())
            self.v = keys[self._pointer]
            self._pointer += 1
            self.used.append(self.v)
            return self.v
        else:
            if self._pointer == len(self._collection[self.v]) + 1:
                if not self._vr:
                    raise StopIteration
                else:
                    self.v = self._vr[0]
                    self._vr = self._vr[1:]
                    self._pointer = 1
            if not self._collection[self.v]:
                return self.__next__()
            a = self._collection[self.v][self._pointer-1]
            if a not in self.used:
                self._vr.append(self._collection[self.v][self._pointer-1])
                self._pointer += 1
                self.used.append(a)
                return a
            self._pointer += 1
            return self.__next__()


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        return Graph_iter(self.E, 0)

E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)
for vertex in graph:
    print(vertex)