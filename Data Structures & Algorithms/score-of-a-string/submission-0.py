class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for x in range(1, len(s)):
            print(ord(s[x]))

            prev = s[x-1]
            current = s[x]
            result = ord(s[x]) - ord(s[x-1])

            print("per result", result)
            total += abs(result)
        return total