class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        minutes, fresh_fruit = 0, 0
        q = deque() # (r, c)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruit += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh_fruit > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in neighbors:
                    new_r, new_c = r + dr, c + dc
                    if (min(new_r, new_c) < 0 or
                        new_r == ROWS or new_c == COLS or
                        grid[new_r][new_c] != 1):
                        continue
                    
                    q.append((new_r, new_c))
                    grid[new_r][new_c] = 2
                    fresh_fruit -= 1

            minutes += 1

        return minutes if fresh_fruit == 0 else -1




        