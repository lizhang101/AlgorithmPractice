from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # --------------

    def BFS(self, u):
        """
        breath first search from a given node u.
        :param u: node id to start
        :return: None
        """
        print("BFS")
        # put the start node into the queue
        queue = [u]
        # store the visited flags for each node
        visited = {}
        while queue:
            # visit each node once in the queue
            q = queue.pop(0)
            # post order
            # visited[q] = True
            for n in self.graph[q]:
                if not visited.get(n, False):
                    print(q, "->", n)
                    queue.append(n)
                    visited[n] = True

    def DFS(self, u):
        """
        depth first search from a given node u
        :param u:
        :return:
        """
        print("DFS")
        visited = {}

        def _dfs_(u):
            for n in self.graph[u]:
                if not visited.get(n, False):
                    print(n)
                    visited[n] = True
                    _dfs_(n)

        _dfs_(u)

    def find_parent(self, parent, i):
        p = i
        while parent[p] != -1:
            p = parent[p]
        return p

    def union (self, parent, x, y):
        x_set = self.find_parent(parent, x)
        y_set = self.find_parent(parent, y)
        parent[x_set] = y_set

    # according to geeksforgeeks.
    # What if there are multiple parents for one vertex?
    #      This single parent array may not work.
    #      One way is to use an ID to represent a set, and put this ID into the parent array.
    #      In this case, it's not the parent anymore.
    #      Problem is when we need to union the set, we'll have to search all the array and change to set ID to
    #      union 2 sets.
    #      Another way is we really use Set. If u, v are connected, put them into the same set and make parent[u] = parent[v] = this_set.
    #      If we need to union 2 vertices' set, we'll need to first union the set that they are referring to, and change each vertex in both sets,
    #      and let them refer to the union set.
    def undirect_cyclic(self):
        """
        Treat the graph as an undirected graph, count how many circles in this graph.

        :param u:
        :return:
        """

        parent = [-1] * len(self.graph)

        circles = 0
        for v in self.graph:
            for u in self.graph[v]:
                x = self.find_parent(parent, v)
                y = self.find_parent(parent, u)
                if x == y:
                    circles += 1
                self.union(parent, u, v)
        print("undirect graph, circles:", circles)
        return circles

    # Another solution is "colored" vertices. Idea is similar.
    # When start visiting a vertex, mark it as "gray". And mark it as "black" when finished all its descendents processing.
    # All vertices are marked as "white" at beginning.
    def direct_cyclic(self):
        """
        count circles.
        Based on DFS. Added anohter flag array: recursive_visited.
        When starting visiting a vertex, add it to rec_visited. if a vertex is visited, and also in rec_visited,
        that means there is a back edge in the visiting.
        remove the vertex from rec_visited after all its descendents are processed.
        :return:
        """

        def _dfs_cyclic(visited, rec_visited, u):
            visited[u] = True
            rec_visited[u] = True
            circles = 0
            for v in self.graph[u]:
                if not visited[v]:
                    circles += _dfs_cyclic(visited, rec_visited, v)
                elif rec_visited[v]:
                    circles += 1
            rec_visited[u] = False
            return circles

        visited = [False] * len(self.graph)
        rec_visited = [False] * len(self.graph)
        circles = 0
        for u in self.graph:
            circles += _dfs_cyclic(visited, rec_visited, u)
        print("direct_cyclic:", circles)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.BFS(2)
g.DFS(2)
g.direct_cyclic()

g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

g.undirect_cyclic()
