class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        ROWS, COLS = len(grid), len(grid[0])

        guard_set = set(map(tuple, guards))
        wall_set = set(map(tuple, walls))

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in guard_set:
                    grid[r][c] = 1
                elif (r, c) in wall_set:
                    grid[r][c] = 2
                else:
                    grid[r][c] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                while (0 <= nr < ROWS and
                       0 <= nc < COLS and
                       grid[nr][nc] not in (1, 2)):

                       grid[nr][nc] = 3
                       nr += dr
                       nc += dc

        count = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    count += 1

        return count

        



