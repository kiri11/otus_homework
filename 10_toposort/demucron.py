from typing import List


def make_graph(edges, n):
    g = [[] for _ in range(n)]
    for a, b in edges:
        g[a].append(b)
    return g


def graph_to_adj_matrix(graph: list):
    n = len(graph)
    adj_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in graph[i]:
            adj_matrix[i][j] = 1
    return adj_matrix


def edges_to_adj_matrix(n: int, edges: list):
    adj_matrix = [[0] * n for _ in range(n)]
    for a, b in edges:
        adj_matrix[b][a] = 1
    return adj_matrix


def demurcon(adj_matrix: List[List[int]]):
    adj_matrix_transposed = zip(*adj_matrix)
    in_counts = [sum(line) for line in adj_matrix_transposed]
    n = len(adj_matrix)
    result = []
    while len(result) < n:
        has_cycle = True
        for v, cnt in enumerate(in_counts):
            if cnt == 0:
                # remove line v
                for i in range(n):
                    in_counts[i] -= adj_matrix[v][i]
                in_counts[v] = -1  # processed
                result.append(v)
                has_cycle = False
        if has_cycle:
            return []
    return result


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = make_graph(prerequisites, numCourses)
        adj_matrix = graph_to_adj_matrix(graph)
        return demurcon(adj_matrix)


print(Solution().findOrder(2, [[1,0],] ))
print(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(Solution().findOrder(2, [[0,1],[1,0]]))