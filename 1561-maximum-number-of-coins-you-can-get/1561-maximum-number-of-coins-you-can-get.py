import numpy as np
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles)
        count = 0
        for i in range(int(len(piles)/3), len(piles), 2):
            count += sorted_piles[i]
        return count
            