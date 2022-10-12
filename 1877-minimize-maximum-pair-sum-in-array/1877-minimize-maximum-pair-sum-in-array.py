import math 
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        i, j = 0, len(sorted_nums)-1
        max_min_sum = 0

        while i<j:
            max_min_sum = max(max_min_sum, sorted_nums[i] + sorted_nums[j])
            i += 1
            j -= 1
        return max_min_sum
        
            
            
            