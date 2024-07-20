class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool """
        for i,v in enumerate(matrix):
                try:
                    s = v.index(target)
                except:
                    continue
                print(f"{i} and {s}") 
                break
a = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]; target = 16
a.searchMatrix(matrix,target)
        