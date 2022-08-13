import torch
from typing import Optional, Union


class Graph(object):
    def __init__(self, vertex: list(str), nodes) -> None:
        assert(len(vertex) == len(nodes))
        self.dim = len(vertex)
        self.vertex = vertex
        self.nodes = nodes
        self.index_dict = {self.vertex[i]: i for i in range(len(self.vertex))}

    def __getitem__(self, vertex: Optional[Union[str, int]]):
        if isinstance(vertex, str):
            return self.nodes[self.index_dict[vertex]]
        elif isinstance(vertex, int):
            return self.nodes[vertex]
        else:
            raise TypeError("Wrong type of vertex")
        
    @property
    def adjacent_matrix(self):
        adj_mat = [[0 for _ in range(self.dim)] for _ in range(self.dim)]
        for i in range(self.dim):
            for neigh in self.ndoes[i]:
                adj_mat[i][neigh] = 1
                adj_mat[neigh][i] = 1
                
        return adj_mat
    
    @property
    def degree_matrix(self):
        degree_mat = [[0 for _ in range(self.dim)] for _ in range(self.dim)]
        for i in range(self.dim):
            degree_mat[i][i] = len(self.nodes[i])
        return degree_mat
