class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=[]
        column=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.append(i)
                    column.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in row or j in column:
                        matrix[i][j]=0
        print(matrix)
        