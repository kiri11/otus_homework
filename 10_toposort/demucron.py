from typing import List


def graph_to_adj_matrix(graph: List[List[int]]):
    n = len(graph)
    adj_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            adj_matrix[i][j] = 1
    return adj_matrix


def demurcon(adj_matrix: List[List[int]]) -> List[List[int]]:
    adj_matrix_transposed = zip(*adj_matrix)
    in_counts = [sum(line) for line in adj_matrix_transposed]
    n = len(adj_matrix)
    levels = []
    while len(levels) < n:
        for v, cnt in enumerate(in_counts):
            levels.append([])
            if cnt == 0:
                # remove line v
                for i in range(n):
                    in_counts[i] -= adj_matrix[v][i]
                in_counts[v] = -1  # processed
                levels[-1].append(v)
        if not levels[-1]:
            # if nothing added, we have a cycle, can't sort
            return []
    return levels


def toposort(graph: List[List[int]]) -> List[List[int]]:
    adj_matrix = graph_to_adj_matrix(graph)
    return demurcon(adj_matrix)
