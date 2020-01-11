"""Prim’s Minimum Spanning Tree
A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is
    a spanning tree with weight less than or equal to the weight of every other spanning tree.
The weight of a spanning tree is the sum of weights given to each edge of the spanning tree
A minimum spanning tree has (V – 1) edges where V is the number of vertices in the given graph.

"""

from collections import defaultdict
import sys


class Graph:
    """
    store as  list of edges
    """

    def __init__(self, vertices):
        self.num_vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def print_mst(self, parent):
        print("edge\tweight")
        for i in range(1, self.num_vertices):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def min_key(self, key, mst):
        min_key = sys.maxsize
        min_index = 0
        for u in range(self.num_vertices):
            if key[u] < min_key and not mst[u]:
                min_key = key[u]
                min_index = u

        return min_index

    def prim_mst(self):
        """
        1. starts from the node u with minimal key. Add u into MST
        2. explore the neighbors of the node u. Update the key and parent for each neighbor, make sure it always has the
           smallest key and store that parent.
        3. for each neighbor v, if it's not in MST, check if its key is greater than the weight of u to v.
           If yes, need to update key[v], and mark parent[v] as u.
        :return:
        """
        key = [sys.maxsize] * self.num_vertices
        parent = [None] * self.num_vertices  # array for constructed MST
        key[0] = 0  # set source key to be 0 so it will be picked up first
        mst = [False] * self.num_vertices

        for c in range(self.num_vertices):
            u = self.min_key(key, mst)
            mst[u] = True

            for v in range(self.num_vertices):
                if self.graph[u][v] > 0 and not mst[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0],
           ]

g.prim_mst()
