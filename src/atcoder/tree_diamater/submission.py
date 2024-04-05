import random
from collections import defaultdict
from math import inf
from sys import stdin
from typing import List


class FastIO:
    def __init__(self):
        self.random_seed = random.randint(0, 10 ** 9 + 7)
        return

    @staticmethod
    def read_int():
        return int(stdin.readline().rstrip())

    @staticmethod
    def read_float():
        return float(stdin.readline().rstrip())

    @staticmethod
    def read_list_ints():
        return list(map(int, stdin.readline().rstrip().split()))

    @staticmethod
    def read_list_ints_minus_one():
        return list(map(lambda x: int(x) - 1, stdin.readline().rstrip().split()))

    @staticmethod
    def read_str():
        return stdin.readline().rstrip()

    @staticmethod
    def read_list_strs():
        return stdin.readline().rstrip().split()

    @staticmethod
    def st(x):
        return print(x)

    @staticmethod
    def lst(x):
        return print(*x)

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a, b):
        return a if a < b else b

    @staticmethod
    def ceil(a, b):
        return a // b + int(a % b != 0)

    @staticmethod
    def accumulate(nums):
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        return pre


class UnionFind:
    def __init__(self, n: int) -> None:
        self.root_or_size = [-1] * n
        self.part = n
        self.n = n
        return

    def initialize(self):
        for i in range(self.n):
            self.root_or_size[i] = -1
        self.part = self.n
        return

    def find(self, x):
        y = x
        while self.root_or_size[x] >= 0:
            # range_merge_to_disjoint to the direct root node after query
            x = self.root_or_size[x]
        while y != x:
            self.root_or_size[y], y = x, self.root_or_size[y]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.root_or_size[root_x] < self.root_or_size[root_y]:
            root_x, root_y = root_y, root_x
        self.root_or_size[root_y] += self.root_or_size[root_x]
        self.root_or_size[root_x] = root_y
        self.part -= 1
        return True

    def union_left(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.root_or_size[root_x] += self.root_or_size[root_y]
        self.root_or_size[root_y] = root_x
        self.part -= 1
        return True

    def union_right(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.root_or_size[root_y] += self.root_or_size[root_x]
        self.root_or_size[root_x] = root_y
        self.part -= 1
        return True

    def union_max(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if root_x > root_y:
            root_x, root_y = root_y, root_x
        self.root_or_size[root_y] += self.root_or_size[root_x]
        self.root_or_size[root_x] = root_y
        self.part -= 1
        return

    def union_min(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if root_x < root_y:
            root_x, root_y = root_y, root_x
        self.root_or_size[root_y] += self.root_or_size[root_x]
        self.root_or_size[root_x] = root_y
        self.part -= 1
        return

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root_or_size[self.find(x)]

    def get_root_part(self):
        # get the nodes list of every root
        part = defaultdict(list)
        n = len(self.root_or_size)
        for i in range(n):
            part[self.find(i)].append(i)
        return part

    def get_root_size(self):
        # get the size of every root
        size = defaultdict(int)
        n = len(self.root_or_size)
        for i in range(n):
            if self.find(i) == i:
                size[i] = -self.root_or_size[i]
        return size


class TreeDiameter:
    def __init__(self, dct):
        self.n = len(dct)
        self.dct = dct
        return

    def get_bfs_dis(self, root):
        dis = [inf] * self.n
        stack = [root]
        dis[root] = 0
        parent = [-1] * self.n
        while stack:
            i = stack.pop()
            for j, w in self.dct[i]:  # weighted edge
                if j != parent[i]:
                    parent[j] = i
                    dis[j] = dis[i] + w
                    stack.append(j)
        return dis, parent

    def get_diameter_info(self):
        """get tree diameter detail by weighted bfs twice"""
        dis, _ = self.get_bfs_dis(0)
        x = dis.index(max(dis))
        dis, parent = self.get_bfs_dis(x)
        y = dis.index(max(dis))
        path = [y]
        while path[-1] != x:
            path.append(parent[path[-1]])
        path.reverse()
        return x, y, path, dis[y]


def standard_procedure(edges: List[int], n: int) -> int:
    dct = [[] for _ in range(n)]
    for i, j, w in edges:
        dct[i].append((j, w))
        dct[j].append((i, w))
    father = [-1] * n
    stack = [(0, -1)]
    sub = [[0, 0, 0] for _ in range(n)]
    dia = [0] * n
    while stack:
        x, fa = stack.pop()
        if x >= 0:
            stack.append((~x, fa))
            for y, w in dct[x]:
                if y != fa:
                    stack.append((y, x))
                    father[y] = x
        else:
            x = ~x
            a = b = c = d = 0
            for y, ww in dct[x]:
                if y != fa:
                    for w in sub[y][:1]:
                        if w + ww >= a:
                            a, b, c = w + ww, a, b
                        elif w + ww >= b:
                            b, c = w + ww, b
                        elif w + ww >= c:
                            c = w + ww
                    d = max(d, dia[y])
            sub[x] = [a, b, c]
            d = max(d, a + b)
            dia[x] = d

    ans = inf
    stack = [(0, -1, 0, 0)]
    while stack:
        x, fa, pre, pre_dia = stack.pop()
        a, b, c = sub[x]
        aa = bb = -inf
        for y, _ in dct[x]:
            if y != fa:
                dd = dia[y]
                if dd >= aa:
                    aa, bb = dd, aa
                elif dd >= bb:
                    bb = dd
        for y, w in dct[x]:
            if y != fa:
                down = dia[y]
                if sub[y][0] == a - w:
                    up = max(pre + b, b + c, pre_dia)
                    nex = max(pre, b) + w
                    nex_dia = max(pre_dia, pre + b, b + w, b + c)
                elif sub[y][0] == b - w:
                    up = max(pre + a, a + c, pre_dia)
                    nex = max(pre, a) + w
                    nex_dia = max(pre_dia, pre + a, a + w, a + c)
                else:
                    up = max(pre + a, a + b, pre_dia)
                    nex = max(pre, a) + w
                    nex_dia = max(pre_dia, pre + a, a + w, a + b)
                if dia[y] == aa:
                    up = max(up, bb)
                    nex_dia = max(nex_dia, bb)
                else:
                    up = max(up, aa)
                    nex_dia = max(nex_dia, aa)
                ans = min(ans, abs(up - down))
                stack.append((y, x, nex, nex_dia))
    return ans


def brute_force(edges: List[int], n: int) -> int:
    ans = inf
    for i in range(n - 1):
        uf = UnionFind(n)
        for j in range(n - 1):
            if i != j:
                x, y, _ = edges[j]
                uf.union(x, y)
        group = uf.get_root_part()
        assert uf.part == 2
        cur = []
        for g in group:
            lst = group[g]
            m = len(lst)
            ind = {num: i for i, num in enumerate(lst)}
            dct = [[] for _ in range(m)]
            for index, (x, y, w) in enumerate(edges):
                if index == i:
                    continue
                if uf.find(x) == g:
                    dct[ind[x]].append((ind[y], w))
                    dct[ind[y]].append((ind[x], w))
            dia = TreeDiameter(dct)
            cur.append(dia.get_diameter_info()[-1])
        ans = min(ans, max(cur) - min(cur))
    return ans


class Solution:
    def __init__(self):
        return

    @staticmethod
    def main(ac=FastIO()):
        n = ac.read_int()
        edges = [ac.read_list_ints() for _ in range(n - 1)]
        assert 2 <= n <= 2 * 10 ** 5
        assert all(0 <= x < n and 0 <= y < n and 1 <= w <= 10 ** 9 for x, y, w in edges)
        ans = brute_force(edges, n)
        ac.st(ans)
        return


Solution().main()
