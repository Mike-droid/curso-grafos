from queue import Queue
from typing import List


class Solution:
  def minimum_knight_moves(self, target: List[int]) -> int:
    # The knight moves in 8 possible directions
    directions = [
      (2, 1), (2, -1), (-2, 1), (-2, -1),
      (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    queue = Queue()
    queue.put((0, 0, 0)) # (current_x, current_y, step_count)
    visited_positions = set()
    visited_positions.add((0, 0))

    target_x, target_y = abs(target[0]), abs(target[1])

    # BFS algorithm
    while not queue.empty():
      # Dequeue the next position and step count to be processed
      current_x, current_y, current_steps = queue.get()

      # Check if we've reached the target position
      if current_x == target_x and current_y == target_y:
        return current_steps

      # Explore all possible knight moves
      for dx, dy in directions:
        new_x = current_x + dx
        new_y = current_y + dy
        new_position = (abs(new_x), abs(new_y))

        # Check if the new position has been visited
        if new_position not in visited_positions:
          visited_positions.add(new_position)
          queue.put((new_x, new_y, current_steps + 1))

# Example usage:
solution = Solution()
print(solution.minimum_knight_moves([2, 1]))  # Output: 1
print(solution.minimum_knight_moves([5, 5]))  # Output: 4
