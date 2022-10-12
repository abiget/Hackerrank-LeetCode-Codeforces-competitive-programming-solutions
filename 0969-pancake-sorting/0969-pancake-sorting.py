import random
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr), 0, -1):
            max_index = arr.index(i)
            res.extend([max_index+1 , i])
            arr = arr[:max_index:-1] + arr[:max_index]
        return res