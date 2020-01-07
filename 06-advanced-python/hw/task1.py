"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной
Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)
"""
import collections


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class Graph:

    def __init__(self, E):
        self.E = E
        self.start = 0
        self.vertex = list(E.keys())

    def bfs(self, start):
        frontier = Queue()
        frontier.put(start)
        visited = []
        visited.append(start)
        while not frontier.empty():
            current = frontier.get()
            for next in self.E[current]:
                if next not in visited:
                    frontier.put(next)
                    visited.append(next)
        return visited

    def __next__(self):
        if self.start < len(self.E):
            self.start += 1
            vertex = self.vertex[self.start - 1]
            return vertex
        else:
            raise StopIteration

    def __iter__(self):
        return self


E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
graph = Graph(E)
print(graph.bfs('A'))

# for vertex in graph:
#     print(vertex)
