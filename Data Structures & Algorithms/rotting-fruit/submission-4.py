class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh_fruit, minutes = 0, 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1

        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh_fruit > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        grid[r + dr][c + dc] != 1):
                        continue
                    
                    grid[r + dr][c + dc] = 2
                    q.append((r + dr, c + dc))
                    fresh_fruit -= 1

            minutes += 1

        return minutes if fresh_fruit == 0 else -1
            

                    
        