class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        time = 0
        freshcount = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])

                if grid[i][j] == 1:
                    freshcount += 1

        while q and freshcount:
            size = len(q)
            time += 1
            for _ in range(size):
                orange = q.popleft()

                for i, j in dirs:
                    nr = i+orange[0]
                    nc = j+orange[1]

                    # boundary check
                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            freshcount -= 1
                            q.append([nr, nc])

        if freshcount == 0:
            return time
        else:
            return -1
