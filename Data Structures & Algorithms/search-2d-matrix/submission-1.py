class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = len(matrix) - 1
        left = 0
        while left <= right:
            mid = (right + left) // 2
            if matrix[mid][len(matrix[mid])-1] >= target and matrix[mid][0] <= target:
                left = 0
                right = len(matrix[mid]) - 1
                while left <= right:
                    mid2 = (right + left) //2
                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] > target:
                        right = mid2-1
                    else:
                        left = mid2+1
                return False


            elif matrix[mid][len(matrix[mid])-1] > target:
                right = mid -1
            else:
                left = mid +1
        return False
            