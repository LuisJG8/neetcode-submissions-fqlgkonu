class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num

        while l <= r:
            mid = l + ((r - l) // 2)
            calc = mid * mid
            if calc > num:
                r = mid - 1
            elif calc < num:
                l = mid + 1
            else:
                return True
        return False