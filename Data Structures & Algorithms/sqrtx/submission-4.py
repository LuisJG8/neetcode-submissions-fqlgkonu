class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            mid = l + ((r - l) // 2)
            double = mid * mid
            if double > x:
                r = mid - 1
            elif double < x:
                l = mid + 1
                res = mid
            else:
                return mid
        return res

        
        #     m = l + (r - l) // 2
        #     if m * m > x:
        #         r = m - 1
        #     elif m * m < x:
        #         l = m + 1
        #         res = m
        #     else:
        #         return m

        # return res