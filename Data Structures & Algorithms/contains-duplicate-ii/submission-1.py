class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # count = []
        # for x, y in enumerate(nums):
        #     if x in count:
        #         return True 
        #     count.append(x)
 

        # nums = [1,2,3,1], k = 3

        window = set()
        L = 0

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False