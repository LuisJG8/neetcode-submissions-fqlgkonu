class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # l, r = 0, len(nums) - 1
        # res = 0

        # while l <= r:
        #     mid = l + ((r - l) // 2)
        #     if mid > target:
        #         r = mid - 1
        #         res = mid
        #     elif mid < target:
        #         l = mid + 1
        #     else:
        #         return mid
        # return res

        res = len(nums)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return l
