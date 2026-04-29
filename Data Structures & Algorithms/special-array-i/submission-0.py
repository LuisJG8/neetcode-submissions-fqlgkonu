class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = []
        for i in range(1, len(nums)):
            if nums[i] % 2 == 1 and nums[i - 1] % 2 == 0 or nums[i] % 2 == 0 and nums[i - 1] % 2 == 1:
                l.append("Valid")
                continue
            else:
                l.append("NotValid")
        if "NotValid" in l:
            return False
        else:
            return True