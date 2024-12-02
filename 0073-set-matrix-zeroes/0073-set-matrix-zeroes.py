def markzero(matrix,row,column,j):#column is fixed just iterate through rows
    for i in range(row):
        if matrix[i][j]!=0:
            matrix[i][j]="x"
def markzeroc(matrix,row,column,i):#row is fixed just iterate through rows
    for j in range(column):
        if matrix[i][j]!=0:
            matrix[i][j]="x"
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    markzero(matrix,len(matrix),len(matrix[0]),j)
                    markzeroc(matrix,len(matrix),len(matrix[0]),i)
       
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="x":
                    matrix[i][j] = 0
        print(matrix)