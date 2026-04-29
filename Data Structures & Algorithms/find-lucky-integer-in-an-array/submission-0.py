class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hm = {}
        for x in arr:
            hm[x] = 1 + hm.get(x, 0)
        res = -1

        for x in hm:
            if x == hm[x]:
                res = max(res, x)
        return res