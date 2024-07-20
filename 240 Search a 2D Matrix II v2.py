class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool """
        rn = len(matrix)
        cn = len(matrix[0])
        i = 0
        j = cn-1
        while j >= 0 and i < rn:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                print(True)
                return True

                


a = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]; target = 133
a.searchMatrix(matrix,target)
        