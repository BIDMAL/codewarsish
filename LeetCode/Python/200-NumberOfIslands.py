from typing import List
from collections import deque
"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all
four edges of the grid are all surrounded by water.
"""


class Solution:  # DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0

        def dfs(i, j):
            grid[i][j] = '2'
            for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                ii, jj = i+di, j+dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == '1':
                    dfs(ii, jj)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans


class SolutionBFS:  # BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q = deque([(i, j)])
                    grid[i][j] = '2'
                    while q:
                        x, y = q.popleft()
                        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                            xx, yy = x+dx, y+dy
                            if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == '1':
                                q.append((xx, yy))
                                grid[xx][yy] = '2'
                    ans += 1
        return ans


class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.n = n
        self.size = n

    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj:
            self.size -= 1
            self.p[pj] = pi

    def find(self, i):
        if i != self.p[i]:
            self.p[i] = self.find(self.p[i])
        return self.p[i]


class SolutionUF:  # Union-Find
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        d = dict()
        idx = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    d[i, j] = idx
                    idx += 1
        uf = UF(idx)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if i > 0 and grid[i-1][j] == '1':
                        uf.union(d[i-1, j], d[i, j])
                    if j > 0 and grid[i][j-1] == '1':
                        uf.union(d[i, j-1], d[i, j])
        return uf.size


def test(input, output):
    solution = Solution()
    out = solution.numIslands(input)
    assert out == output


if __name__ == '__main__':

    test(
        input=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],
        output=1
    )

    test(
        input=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ],
        output=3
    )

    test(
        input=[
            ["1", "1", "1"],
            ["0", "1", "0"],
            ["1", "1", "1"]
        ],
        output=1
    )
