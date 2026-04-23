class Solution:
    def maxDifference(self, s: str) -> int:
        # hashmap = {}
        # res = float("-inf")

        # for x in s:
        #     hashmap[x] = 1 + hashmap.get(0, 1)

        # for even in hashmap.values():
        #     if even % 2 == 1: continue
        #     for odd in hashmap.values():
        #         if odd % 2 == 0: continue
        #         res = max(res, odd - even)
        # return res

        hashmap = {}
        res = float("-inf")

        for x in s:
            hashmap[x] = 1 + hashmap.get(x, 0)

        for even in hashmap.values():
            if even % 2 == 1: continue
            for odd in hashmap.values():
                if odd % 2 == 0: continue
                res = max(res, odd - even)
        return res