from typing import List, Tuple

from utils.disjoint_set import DisjointSet
from utils.generate_graph import generate_graph_image_with_highlights

Node = str

Edge = Tuple[Node, Node, int]


def kruskal(vertices: List[Node], edges: List[Edge]) -> List[Edge]:
    ds = DisjointSet()
    for vertex in vertices:
        ds.make_set(vertex)
    edges.sort(key=lambda e: e[-1])
    mst_edges = []
    for edge in edges:
        src, dest, weight = edge
        if ds.find_set(src) != ds.find_set(dest):
            ds.union(src, dest)
            mst_edges.append(edge)
    return mst_edges


def main():
    nodes = list('abcdefghi')
    edges = [('a', 'b', 4), ('a', 'h', 8), ('b', 'h', 11), ('h', 'i', 7), ('h', 'g', 1), ('i', 'g', 6), ('i', 'c', 2),
             ('c', 'f', 4), ('b', 'c', 8), ('g', 'f', 2), ('c', 'd', 7), ('d', 'e', 9), ('d', 'f', 14), ('f', 'e', 10)]
    mst_edges = kruskal(nodes, edges)
    generate_graph_image_with_highlights(edges, mst_edges)


if __name__ == '__main__':
    main()
