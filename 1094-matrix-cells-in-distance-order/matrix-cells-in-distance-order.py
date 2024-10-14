class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        matrix = []
        for i in range(rows):
            for j in range(cols):
                distance = abs(i-rCenter) + abs(j-cCenter)
                
                matrix.append([i,j,distance])
        matrix.sort(key = lambda t:t[2])
        for i in range(len(matrix)):
            newval = [matrix[i][0],matrix[i][1]]
            matrix[i] = newval
        return matrix