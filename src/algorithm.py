import numpy as np
from utils.graph import Graph


class PageRank(object):
    """
    Implememt of Page Rank algorithm
    Args:
        `graph` (`Graph`): given graph of PageRank
        `beta`: const used in matrix A
        `max_iter` (`int`): max iteration steps
        `epsilon`: threshold used in iteration
    """
    def __init__(self, graph: Graph, beta, max_iter: int = 1000, epsilon = 1e-5) -> None:
        self.graph = graph
        self.dim = self.graph.dim
        self.adj_mat = np.array(self.graph.adjacent_matrix)
        self.degree_mat = np.array(self.graph.degree_matrix)
        self.M = np.array(self.graph.stochastic_adjacency_matrix)
        self.max_iter = max_iter
        self.pagerank_vec = np.zeros((self.dim, 1))
        self.beta = beta
        self.one_vec = np.ones((self.dim, 1))
        # Recall that the equation need to solve is r = Ar
        self.A = self.beta * self.M +\
            (1 - self.beta) / self.dim * (self.one_vec @ self.one_vec.T)
        
    def solve(self):
        pass
        