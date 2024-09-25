from queue import Queue
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rotten_oranges = Queue()
        fresh_oranges = 0
        minutes_passed = 0

        for i, row in enumerate(grid):
            for j, orange in enumerate(row):
                if orange == 1:
                    fresh_oranges += 1
                if orange == 2:
                    rotten_oranges.put((i,j))

        if fresh_oranges == 0:
            return 0

        while not rotten_oranges.empty():
            size = rotten_oranges.qsize()
            new_rotting = False
            for _ in range(size):
                x,y = rotten_oranges.get()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        rotten_oranges.put((nx, ny))
                        new_rotting = True
            if new_rotting:
                minutes_passed += 1
        if fresh_oranges > 0:
            return -1
        else:
            return minutes_passed

if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(f"Minutes needed: {solution.orangesRotting(grid)}")  # Expected output: 4

    # Test Case 2
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(f"Minutes needed: {solution.orangesRotting(grid)}")  # Expected output: -1

    # Test Case 3
    grid = [[0, 2]]
    print(f"Minutes needed: {solution.orangesRotting(grid)}")  # Expected output: 0

