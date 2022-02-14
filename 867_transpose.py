class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        # for i in range(len(matrix)):
        #     for j in range(i+1, len(matrix)):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # return matrix
        
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix))]

        # Time Complexity: O(r*c)
        # Space Complexity: O(1)
