from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []


        result = []

        def backtrack(start: int, path: List[str]):
            if len(path) == 4 and start == len(s):
                result.append(".".join(path))
                return

            if len(path) == 4:
                return

            for length in range(1,4):
                if start + length <= len(s):
                    segment = s[start:start + length]
                    if (len(segment) > 1 and segment[0] == "0" or int(segment) > 255):
                        continue
                    backtrack(start + length, path + [segment])


        backtrack(0, [])
        return result


solution = Solution()
solution.restoreIpAddresses("25525511135")
solution.restoreIpAddresses("0000")
solution.restoreIpAddresses("101023")
