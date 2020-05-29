from math import sqrt
from itertools import combinations, permutations


class Graph:
    def __init__(self, v_num):
        self.graph = [[0.] * v_num for _ in range(v_num)]

    def __str__(self):
        return "\n".join([" ".join(map(lambda x: "%.2f" % x, row)) for row in self.graph])

    @staticmethod
    def dist(p1, p2):
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def TSP(self):
        min_cost = float('inf')
        min_perm = None

        for perm in permutations(tuple(range(n))):
            cost = 0
            perm_mutable = list(perm)

            while len(perm_mutable) != 1:
                start = perm_mutable.pop(0)
                fin = perm_mutable[0]
                cost += g.graph[start][fin]

            cost += g.graph[perm[-1]][perm[0]]

            if cost < min_cost:
                min_perm = perm
                min_cost = cost
        return min_cost, min_perm


fin = open('coord.txt')
n = int(fin.readline())

coords = []

for num, line in enumerate(fin):
    coords.append(tuple([*map(int, line.split()), num]))

print(coords)
g = Graph(n)
# weight matrix
for combination in combinations(coords, 2):
    g.graph[combination[0][2]][combination[1][2]] = g.dist(combination[0], combination[1])
    g.graph[combination[1][2]][combination[0][2]] = g.dist(combination[0], combination[1])

print('Distance matrix: \n', g, sep='')

cost, perm = g.TSP()

print(f'Cost: {cost}, path: {" - ".join(map(str, map(lambda x: x+1, perm)))} - {perm[0] + 1}')
