class GraphNode:
    def __init__(self, x):
        self.key = x
        self.neighbors = []

def bfs_copy(graph):
    copied = []
    track = {}
    for s in graph:
        if s in track:
            continue
        else:
            queue = [s]
            track[s] = GraphNode(s.key)
            while queue:
                u = queue.pop(0)
                copied.append(track[u])
                print(u.key)
                for v in u.neighbors:
                    if track.get(v, None) is None:
                        queue.append(v)
                        v_copy = GraphNode(v.key)
                        track[v] = v_copy

                    track[u].neighbors.append(track[v])

def dfs_copy(graph):
    def _copy_(copy_to, u, track):
        track[u] = GraphNode(u.key)
        copy_to.append(track[u])
        for v in u.neighbors:
            if v not in track:
                _copy_(copy_to, v, track)
            track[u].neighbors.append(track[v])

    track = {}
    copy_to = []
    for u in graph:
        if u not in track:
            _copy_(copy_to, u, track)

    return copy_to




n0 = GraphNode(0)
n1 = GraphNode(1)
n2 = GraphNode(2)
n0.neighbors = [n1, n2]
n1.neighbors = [n0, n2]
n2.neighbors = [n0, n1]

n4 = GraphNode(4)

graph = [n1,n2,n0,n4]

#copyied1 = bfs_copy(graph)
#copyied2 = bfs_copy(copyied1)

copyied1 = dfs_copy(graph)
copyied2 = dfs_copy(copyied1)

bfs_copy(copyied1) #just for printing





