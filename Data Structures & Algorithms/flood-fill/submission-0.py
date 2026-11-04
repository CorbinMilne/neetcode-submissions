class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        target = image[sr][sc]

        def dfs(r, c, image, visit):
            ROWS, COLS = len(image), len(image[0])

            if (min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or
                image[r][c] != target):
                return

            image[r][c] = color
            visit.add((r, c))

            dfs(r + 1, c, image, visit)
            dfs(r - 1, c, image, visit)
            dfs(r, c + 1, image, visit)
            dfs(r, c - 1, image, visit)

        dfs(sr, sc, image, set())
        return image



        