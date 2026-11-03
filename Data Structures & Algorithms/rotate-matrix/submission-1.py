class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        left, right = 0, len(matrix) - 1

        while left < right:
            top, bottom = left, right

            for i in range(right - left):

                # save topLeft value
                topLeft = matrix[top][left + i]
                # move bottomLeft to topLeft
                matrix[top][left + i] = matrix[bottom - i][left]
                # move bottomRight to bottomLeft
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # move topRight to bottomRight
                matrix[bottom][right - i] = matrix[top + i][right]
                # move saved topLeft to topRight
                matrix[top + i][right] = topLeft
            
            right -= 1
            left += 1
        

        