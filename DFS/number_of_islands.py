from typing import List


class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    islands_counter = 0
    def DFS(i, j):
      if grid[i][j] == '0':
        return

      grid[i][j] = '0'
      # go up
      if i -1 >= 0:
        DFS(i-1, j)
      # go down
      if i + 1 < len(grid):
        DFS(i+1, j)
      # go left
      if j - 1 >= 0:
        DFS(i, j-1)
      # go right
      if j + 1 < len(grid[i]):
        DFS(i, j+1)


    if grid is None or not grid:
      return 0

    for i in range(len(grid)):
      for j in range(len(grid[i])):
        if grid[i][j] == '1':
          DFS(i,j)
          islands_counter += 1

    return islands_counter


if __name__ == "__main__":
    solution = Solution()  # Instantiate the Solution class

    # Example 1
    grid1 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print("Number of islands in grid1: ", solution.numIslands(grid1))

    # Example 2
    grid2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print("Number of islands in grid2: ", solution.numIslands(grid2))

    # Example 3 - Edge case (empty grid)
    grid3 = []
    print("Number of islands in grid3: ", solution.numIslands(grid3))

    # Example 4 - Edge case (all water)
    grid4 = [
      ["0","0","0","0"],
      ["0","0","0","0"]
    ]
    print("Number of islands in grid4: ", solution.numIslands(grid4))
