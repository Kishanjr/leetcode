# TC : O(mn)
# SC : O(mn)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        self.m = len(grid)
        self.n = len(grid[0])
        self.dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self, grid, i, j):
        if grid[i][j] == "0":
            return

        grid[i][j] = "0"

        for ni, nj in self.dirs:
            nr = i+ni
            nc = j+nj

            if 0 <= nr < self.m and 0 <= nc < self.n:
                self.dfs(grid, nr, nc)
