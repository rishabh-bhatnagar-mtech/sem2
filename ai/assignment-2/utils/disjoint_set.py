from typing import Any

Node = Any


class DisjointSet:
    def __init__(self):
        # Parent stores the nodes of all the sets.
        # For a node with no parent, it stores the size of the set
        self.parent = dict()

    def make_set(self, node: Node):
        """
        Create a new set for the given node
        """
        self.parent[node] = -1

    def union(self, x: Node, y: Node):
        p1 = self.find_set(x)
        p2 = self.find_set(y)
        if p1 != p2:
            p1_size = self.parent[p1]
            self.parent[p1] = p2
            self.parent[p2] += p1_size

    def find_set(self, node: Node) -> Node:
        if self._is_parent(node):
            return node
        return self.find_set(self.parent[node])

    def _is_parent(self, node: Node):
        p = self.parent[node]
        return isinstance(p, int) and p < 0
