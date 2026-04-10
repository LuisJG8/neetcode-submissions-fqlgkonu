class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m = -1

        for i in range(len(arr) - 1, -1, -1):
            newM = max(m, arr[i])
            arr[i] = m
            m = newM
        return arr

        