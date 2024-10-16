from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get dimensions of the board
        rows, cols = len(board), len(board[0])
        
        # Define the backtrack function
        def backtrack(r, c, index):
            # Base case: if index equals the length of the word, we have found the word
            if index == len(word):
                return True
            
            # Check boundaries and if the current cell matches the word character
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            # Mark the cell as visited by changing its value (to avoid revisiting)
            temp = board[r][c]
            board[r][c] = '#'
            
            # Explore the 4 directions: up, down, left, right
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if backtrack(r + dr, c + dc, index + 1):
                    return True
            
            # Restore the cell after exploring
            board[r][c] = temp
            
            return False
        
        # Try to find the word starting from each cell
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True
        
        return False

