class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]

        for x in range(1, len(f) - 1):
            if f[x - 1] == 0 and f[x] == 0 and f[x + 1] == 0:
                f[x] = 1
                n -= 1
        return n <= 0