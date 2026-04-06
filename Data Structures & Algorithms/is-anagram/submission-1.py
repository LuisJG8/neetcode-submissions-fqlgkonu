class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for c in range(len(s)):
            count_s[s[c]] = 1 + count_s.get(s[c], 0)
            count_t[t[c]] = 1 + count_t.get(t[c], 0)
        for d in count_s:
            if count_s[d] != count_t.get(d, 0):
                return False
        
        return True
