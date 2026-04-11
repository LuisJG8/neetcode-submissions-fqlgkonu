class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for x in range(1, len(s)):
            total += abs(ord(s[x]) - ord(s[x-1]))
        return total