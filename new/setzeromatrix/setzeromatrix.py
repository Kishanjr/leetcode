#tc -O(mn)
#sc - O(max(m,n))

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # Get the dimensions of the matrix
        m = len(matrix)
        n = len(matrix[0])

        # Initialize rowSet and colSet to False for each row and column
        rowSet = [False]*m
        colSet = [False]*n

        # Traverse the matrix and set rowSet[i] and colSet[j] to True for each element matrix[i][j] that is 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowSet[i] = True
                    colSet[j] = True

            # If rowSet[i] is True, set all elements in the ith row to 0
            if rowSet[i]:
                matrix[i] = [0] * n

        # Traverse the matrix again and set matrix[i][j] to 0 for each (i,j) such that rowSet[i] is False and colSet[j] is True
        for i in range(m):
            if rowSet[i]:
                continue
            for j in range(n):
                if colSet[j]:
                    matrix[i][j] = 0
