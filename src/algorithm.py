import numpy as np


class PageRank(object):
    def __init__(self, max_iter: int = 1000) -> None:
        self.max_iter = max_iter
        
    def slove(self):
        