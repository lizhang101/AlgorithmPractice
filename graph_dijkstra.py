import sys


class Graph:
    def __init__(self, vertices):
        self.num_vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist):
        print("node \t dist from source")
        for i in range(self.num_vertices):
            print(i, "\t", dist[i])

    def min_distance(self, dist, spt):
        # find the node in the non-SPT set which has the minimum distance
        mdist = sys.maxsize
        min_index = 0
        for u in range(self.num_vertices):
            if dist[u] < mdist and not spt[u]:
                mdist = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        # initialize dist to inf except the source,
        # so source will be picked first.
        dist = [sys.maxsize] * self.num_vertices
        dist[src] = 0
        spt = [False] * self.num_vertices

        for c in range(self.num_vertices):
            # pick the node with min distance, and add it to spt set.
            u = self.min_distance(dist, spt)
            spt[u] = True

            for v in range(self.num_vertices):
                # u, v has connection
                # v is not in spt
                if self.graph[u][v] > 0 and not spt[v] and \
                                dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
