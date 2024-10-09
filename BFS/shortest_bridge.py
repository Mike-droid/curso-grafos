from typing import List
from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Step 1: Find the first island and mark it, adding boundary cells to the queue
        found = False
        queue = deque()  # Boundary of the first island for expansion
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    self.mark_first_island(grid, i, j, queue)  # Mark first island and add boundaries to queue
                    found = True
                    break
            if found:
                break

        # Step 2: Expand BFS from the first island to reach the second island
        return self.expand(grid, queue)

    def mark_first_island(self, grid: List[List[int]], x: int, y: int, queue: deque):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        grid[x][y] = 2  # Mark the island as visited
        queue_for_marking = deque([(x, y)])

        while queue_for_marking:
            x, y = queue_for_marking.popleft()
            for direction in directions:
                new_x, new_y = x + direction[0], y + direction[1]
                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                    if grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2  # Mark connected land
                        queue_for_marking.append((new_x, new_y))
                    elif grid[new_x][new_y] == 0:
                        # Add boundary water cells to queue for BFS expansion
                        queue.append((x, y))

    def expand(self, grid: List[List[int]], queue: deque) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        steps = 0

        # Start BFS to expand towards the second island
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for direction in directions:
                    new_x, new_y = x + direction[0], y + direction[1]
                    if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                        if grid[new_x][new_y] == 1:  # Found the second island
                            return steps
                        if grid[new_x][new_y] == 0:  # Expand to water, turn it into land
                            grid[new_x][new_y] = 2
                            queue.append((new_x, new_y))
            steps += 1  # Increase the step count as we expand one layer outwards

        return -1  # Should never reach here if there are two islands
