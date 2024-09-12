# Definition for a binary tree node.
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def dfs(node, current_number):
      if not node:
        return 0

      current_number = current_number * 10 + node.val

      if not node.left and not node.right:
        return current_number

      return dfs(node.left, current_number) + dfs(node.right, current_number)

    return dfs(root, 0)


root1 = TreeNode(1, 2, 3)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
solution = Solution()
result = solution.sumNumbers(root1)
print(f'result: {result}')