class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR, countM = {}, {}

        for c in ransomNote:
            countR[c] = 1 + countR.get(c, 0)
        
        for c in magazine:
            countM[c] = 1 + countM.get(c, 0)

        for x in countR:
            if countM.get(x, 0) < countR[x]:
                return False
        return True
