from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = {
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z']
        }

        result = []
        mixing = []

        if not digits:
            return []

        def backtrack(index):
            if index == len(digits):
                result.append("".join(mixing))
                return

            current_digit = int(digits[index])
            letters = combinations[current_digit]

            for letter in letters:
                mixing.append(letter)
                backtrack(index + 1)
                mixing.pop()

        backtrack(0)
        return result


solution = Solution()
print(solution.letterCombinations("69"))
