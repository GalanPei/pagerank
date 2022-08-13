import torch
from typing import Optional, Union


class Graph(object):
    """
    A compact implement of graph for given vertex and nodes
    Args:
        `nodes`: neighours for each vertex
        `vertex`: vertex list of graph.
    """

    def __init__(self, nodes, vertex = None) -> None:
        assert (len(vertex) == len(nodes))
        self.dim = len(vertex)
        self.vertex = vertex
        
        if isinstance(nodes, dict):
            self.nodes = nodes
        elif isinstance(nodes, list):
            self.nodes = {vertex[i]: nodes[i] for i in range(len(nodes))}
        else:
            raise TypeError("Nodes should be either dict or list")

    def __getitem__(self, vertex):
        return self.nodes[vertex]
        
    @property
    def adjacent_matrix(self):
        adj_mat = [[0 for _ in range(self.dim)] for _ in range(self.dim)]
        for i in range(self.dim):
            for neigh in self.nodes[i]:
                adj_mat[i][neigh] = 1
                adj_mat[neigh][i] = 1

        return adj_mat

    @property
    def degree_matrix(self):
        degree_mat = [[0 for _ in range(self.dim)] for _ in range(self.dim)]
        for i in range(self.dim):
            degree_mat[i][i] = len(self.nodes[i])
        return degree_mat

    @property
    def stochastic_adjacency_matrix(self):
        sto_adj_mat = [[0 for _ in range(self.dim)] for _ in range(self.dim)]
        for i in range(self.dim):
            for j in range(self.dim):
                if self.adjacent_matrix[i][j]:
                    sto_adj_mat[i][j] = 1 / self.degree_matrix[j][j]
        return sto_adj_mat
