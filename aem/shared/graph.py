import numpy as np


class Graph:

    def __init__(self, adjacency_matrix, coords):
        self.adjacency_matrix = adjacency_matrix
        self.coords = coords
        self.cache = {}

    def get_closest_neighbor_idx(self, from_vertex):
        if from_vertex in self.cache:
            return self.cache[from_vertex]
        valid_indices = np.where(self.adjacency_matrix[from_vertex, :] != 0)[0]
        closest_idx = valid_indices[self.adjacency_matrix[from_vertex, :][valid_indices].argmin()]
        self.cache[from_vertex] = closest_idx
        return closest_idx

    def get_closest_unvisited_neighbor_idx(self, from_vertex, visited):
        valid_indices = [idx for idx in range(self.no_of_vertices()) if idx not in visited]
        closest_idx = valid_indices[self.adjacency_matrix[from_vertex, :][valid_indices].argmin()]
        return closest_idx

    def get_closest_visited_idx(self, from_vertex, visited):
        closest_idx = visited[self.adjacency_matrix[from_vertex, :][visited].argmin()]
        return closest_idx

    def no_of_vertices(self) -> int:
        return self.adjacency_matrix.shape[0]

    def compute_cycle_length(self, cycle) -> int:
        cycle_length = 0
        for i in range(len(cycle)):
            v1 = cycle[i]
            v2 = cycle[(i+1) % len(cycle)]
            cycle_length += self.adjacency_matrix[v1, v2]
        return cycle_length

    def cost(self, from_vertex, to_vertex):
        return self.adjacency_matrix[from_vertex, to_vertex]

    def nearest_neighbors(self, v, k):
        valid_indices = np.where(self.adjacency_matrix[v, :] != 0)[0]
        closest_indices = valid_indices[np.argsort(self.adjacency_matrix[v, :][valid_indices])]
        return closest_indices[:k]
