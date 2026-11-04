class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        target = image[sr][sc]

        def dfs(r, c, image):
            ROWS, COLS = len(image), len(image[0])

            if (min(r, c) < 0 or
                r == ROWS or c == COLS or
                image[r][c] != target or
                image[r][c] == color):
                return

            image[r][c] = color

            dfs(r + 1, c, image)
            dfs(r - 1, c, image)
            dfs(r, c + 1, image)
            dfs(r, c - 1, image)

        dfs(sr, sc, image)
        return image



        