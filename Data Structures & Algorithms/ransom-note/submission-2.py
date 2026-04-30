class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # countR, countM = {}, {}

        # for c in ransomNote:
        #     countR[c] = 1 + countR.get(c, 0)
        
        # for c in magazine:
        #     countM[c] = 1 + countM.get(c, 0)

        # for x in countR:
        #     if countM[x] < countR[x]:
        #         return False
        # return True

        countR = Counter(ransomNote)
        countM = Counter(magazine)

        for c in countR:
            if countM[c] < countR[c]:
                return False

        return True