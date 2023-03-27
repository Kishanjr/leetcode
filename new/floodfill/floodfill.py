class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.m = len(image)
        self.n = len(image[0])
        self.starting = image[sr][sc]
        self.image = image
        self.color = color

        if color == image[sr][sc]:
            return image
        self.dfs(sr, sc)

        return image

    def dfs(self, sr, sc):
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.image[sr][sc] = self.color

        for i, j in dirs:  # moving to 4 direction using dirs if possible
            nr = sr + i  # neighbouring row
            nc = sc + j  # neightbouring coloumn
            if 0 <= nr < self.m and 0 <= nc < self.n:  # boundary check
                if self.image[nr][nc] == self.starting:
                    self.dfs(nr, nc)
