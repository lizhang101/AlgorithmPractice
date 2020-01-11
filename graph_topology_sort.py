"""
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices
such that for every directed edge uv, vertex u comes before v in the ordering.
Topological Sorting for a graph is not possible if the graph is not a DAG.
"""
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.num_vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_dfs(self):

        def _dfs_ (u, visited, stack):
            visited[u] = True
            for v in self.graph[u]:
                if not visited[v]:
                    _dfs_(v, visited, stack)
            stack.insert(0, u)

        visited = [False] * self.num_vertices
        stack = []

        for u in range(self.num_vertices):
            if not visited[u]:
                _dfs_(u, visited, stack)

        print (stack)

    def topological_sort_degree(self):
        in_degree = [0] * self.num_vertices

        # calculate the in degree for each vertex
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        queue = []# queue for vertices with indegree == 0
        vcnt = 0# count of visited vertices
        order = []

        for i, n in enumerate(in_degree):
            if n == 0:
                queue.append(i)

        while queue:
            u = queue.pop(0)
            order.append(u)
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

            vcnt += 1

        assert vcnt == self.num_vertices, "vcnt %d total:%d" % (vcnt, self.num_vertices)

        print(order)






g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 3)
g.add_edge(4, 3)
g.add_edge(4, 1)
g.add_edge(2, 0)
g.add_edge(0, 1)

g.topological_sort_dfs()
g.topological_sort_degree()
