"""input data format:
NumNode NumEdges
from_node_id to_node_id token
from_node_id to_node_id token

target: return a maximal product of a pair of friend that share the most many of tokens.
"""
#example: 4 nodes, 5 edges
file = \
"4 5\n\
1 2 1\n\
1 2 2\n\
2 3 1\n\
2 3 3\n\
2 4 3\n"

expect = 6
class graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, fid, tid):
        try:
            self.nodes[fid].add(tid)
        except KeyError:
            self.nodes[fid] = {tid}

def build_pairs(from_id, to_id, token):
    pass

def clac_product(file):
    lines = 0
    for ln in file.split("\n"):
        if ln == "":
            return
        if lines == 0:
            nodes, lines = map(int, ln.split())
        else:
            from_id, to_id, token = map(int, ln.split())
            print(from_id, to_id, token)
            lines -= 1
            from_id, to_id = from_id, to_id if from_id <= to_id else to_id, from_id

clac_product(file)
